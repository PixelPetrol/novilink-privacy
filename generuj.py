"""Generator strony polityki prywatności z PRIVACY.md.

JEDNO ŹRÓDŁO PRAWDY to PRIVACY.md — strona powstaje z niego, żeby obie wersje
nie rozjeżdżały się tak, jak rozjechały się między lipcem a październikiem.
"""
import html
import re

BAZA = '/Users/piotrkorona/Desktop/pliki/codex claude pliki/novilink'
MD = BAZA + '/PRIVACY.md'
HTML = BAZA + '/privacy-site/index.html'

NUMEROWANY = re.compile(r'^\*\*\d+(\.\d+)?\.\*\*')

CSS = """  body{font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif;max-width:800px;margin:0 auto;padding:28px 24px 56px;line-height:1.65;color:#1a2233;background:#fff}
  h1{font-size:25px;line-height:1.3} h2{font-size:17px;margin-top:34px}
  code{background:#f1f2f5;padding:1px 5px;border-radius:4px}
  .muted{color:#6b7280;font-size:14px}
  .punkt{margin:8px 0 8px 18px}
  table{border-collapse:collapse;width:100%;margin:16px 0;font-size:15px}
  th,td{border:1px solid #dde2ea;padding:9px 11px;text-align:left;vertical-align:top}
  th{background:#f6f8fc}
  hr{border:0;border-top:1px solid #e5e7eb;margin:30px 0}
  ul{padding-left:22px} li{margin:6px 0}"""


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
    return t


def main():
    md = open(MD).read()
    tytul = md.split('\n', 1)[0].lstrip('# ').strip()
    # Podtytuł: pierwszy akapit w kursywie tuż pod tytułem (podstawa prawna).
    wstep = re.search(r'^_(.+?)_\n', md[len(tytul):], re.S | re.M)
    wstep = ' '.join(wstep.group(1).split()) if wstep else ''

    body = md.split('\n', 1)[1]
    body = re.sub(r'^_.+?_\n', '', body, flags=re.S | re.M, count=1)

    out, i = [], 0
    linie = body.split('\n')
    while i < len(linie):
        l = linie[i]
        if l.startswith('## '):
            out.append('<h2>' + inline(l[3:].strip()) + '</h2>')
            i += 1
            continue
        if l.strip() == '---':
            out.append('<hr>')
            i += 1
            continue
        if l.startswith('|'):
            wiersze = []
            while i < len(linie) and linie[i].startswith('|'):
                wiersze.append(linie[i])
                i += 1
            out.append('<table>')
            for n, w in enumerate(wiersze):
                kom = [c.strip() for c in w.strip('|').split('|')]
                if set(''.join(kom)) <= set('-: '):
                    continue
                tag = 'th' if n == 0 else 'td'
                out.append('  <tr>' + ''.join(
                    '<%s>%s</%s>' % (tag, inline(c), tag) for c in kom) + '</tr>')
            out.append('</table>')
            continue
        if l.strip() == '':
            i += 1
            continue
        if NUMEROWANY.match(l.strip()):
            akapit = [l.strip()]
            i += 1
            while (i < len(linie) and linie[i].strip()
                   and not NUMEROWANY.match(linie[i].strip())
                   and not linie[i].startswith(('## ', '|'))
                   and linie[i].strip() != '---'):
                akapit.append(linie[i].strip())
                i += 1
            out.append('<p class="punkt">' + inline(' '.join(akapit)) + '</p>')
            continue
        akapit = []
        while (i < len(linie) and linie[i].strip()
               and not linie[i].startswith(('## ', '|'))
               and not NUMEROWANY.match(linie[i].strip())
               and linie[i].strip() != '---'):
            akapit.append(linie[i].strip())
            i += 1
        tekst = ' '.join(akapit)
        if tekst.startswith('- '):
            pozycje = [p.strip() for p in re.split(r'(?:^|\s)- ', tekst) if p.strip()]
            out.append('<ul>' + ''.join('<li>%s</li>' % inline(p) for p in pozycje) + '</ul>')
        else:
            out.append('<p>' + inline(tekst) + '</p>')

    strona = ('<!DOCTYPE html>\n<html lang="pl">\n<head>\n<meta charset="utf-8">\n'
              '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
              '<title>' + html.escape(tytul) + '</title>\n<style>\n'
              + CSS + '\n</style>\n</head>\n<body>\n'
              '<h1>' + html.escape(tytul) + '</h1>\n'
              '<p class="muted">' + html.escape(wstep) + '</p>\n'
              + '\n'.join(out) + '\n\n</body>\n</html>\n')
    open(HTML, 'w').write(strona)
    print('sekcji:', strona.count('<h2>'), '· punktów:', strona.count('class="punkt"'),
          '· znaków:', len(strona))


main()
