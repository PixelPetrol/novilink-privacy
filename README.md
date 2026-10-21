# NoviCloud GO — strona polityki prywatności (GitHub Pages)

Ten folder wystawiamy jako **osobne, publiczne** repozytorium. Dzięki temu
polityka prywatności ma publiczny adres `https://…` (wymagany przez Google Play),
a **repozytorium kodu może pozostać prywatne**.

Plik `index.html` jest **generowany** z `../PRIVACY.md` — jedynego źródła prawdy
polityki. Po każdej zmianie polityki uruchom w tym folderze `python3 generuj.py`
i zacommituj wygenerowany `index.html`. NIE kopiuj tu ręcznie żadnego innego pliku.

---

## Publikacja (jednorazowo, ~5 min)

1. Na https://github.com → **New repository**
   - Nazwa: `novilink-privacy`
   - Widoczność: **Public** (Pages za darmo wymaga publicznego repo)
   - Bez README/.gitignore (dodajemy własne pliki)

2. W terminalu, w TYM folderze (`privacy-site/`):
   ```bash
   git init
   git add index.html README.md
   git commit -m "Polityka prywatności NoviCloud GO"
   git branch -M main
   git remote add origin https://github.com/<TWOJ_LOGIN>/novilink-privacy.git
   git push -u origin main
   ```

3. Na GitHubie: repo → **Settings → Pages**
   - **Source:** `Deploy from a branch`
   - **Branch:** `main`, folder `/ (root)` → **Save**

4. Po ~1 minucie strona będzie pod adresem:
   ```
   https://<TWOJ_LOGIN>.github.io/novilink-privacy/
   ```
   Ten adres wklejasz w **Google Play Console → Polityka prywatności**.

---

## Aktualizacja treści później
Treść zmieniasz **wyłącznie** w `../PRIVACY.md`, a stronę odtwarzasz generatorem.
NIE kopiuj tu ręcznie żadnego innego pliku.
```bash
python3 generuj.py
git commit -am "Aktualizacja polityki prywatności"
git push
```
GitHub Pages odświeży stronę automatycznie w ~1 min.

---

## Uwaga
Ten folder jest celowo w `.gitignore` głównego repo NoviCloud GO (wpis `/privacy-site/`),
żeby nie mieszać prywatnego kodu z publiczną stroną. To dwa niezależne repozytoria.

Nazwa repozytorium i publiczny adres nadal brzmią `novilink-privacy` — zmiana adresu
to osobna decyzja, bo wymaga równoczesnej aktualizacji `app/lib/core/app_info.dart`,
`docs/PLAY-STORE-LISTING.md` oraz pola „Polityka prywatności" w Google Play Console.
