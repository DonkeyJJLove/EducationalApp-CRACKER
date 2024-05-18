
# EducationalApp - CRACKER

EducationalApp to aplikacja dydaktyczna mająca na celu naukę tworzenia plików wykonywalnych (.exe) oraz podstawowych technik łamania zabezpieczeń tych plików. Projekt składa się z dwóch głównych modułów: modułu tworzenia pliku .exe oraz modułu crackowania pliku .exe.

## Struktura Katalogów

```
/EducationalApp
├── /src
│   ├── /exe_creator
│   │   ├── __init__.py
│   │   ├── creator.py
│   ├── /exe_cracker
│   │   ├── __init__.py
│   │   ├── cracker.py
│   ├── main.py
├── /tests
│   ├── test_creator.py
│   ├── test_cracker.py
├── /docs
│   ├── README.md
│   ├── requirements.txt
└── create_structure.ps1
```

## Wymagania

- Python 3.8+
- Windows OS
- PyInstaller (do tworzenia plików .exe)

## Instalacja

1. Sklonuj repozytorium:

   ```bash
   git clone https://github.com/twoje-repozytorium/EducationalApp.git
   ```

2. Przejdź do katalogu projektu:

   ```bash
   cd EducationalApp
   ```

3. Utwórz wirtualne środowisko:

   ```bash
   python -m venv venv
   ```

4. Aktywuj wirtualne środowisko:

   - Windows:

     ```bash
     .env\Scriptsctivate
     ```

5. Zainstaluj wymagane pakiety:

   ```bash
   pip install -r docs/requirements.txt
   ```

## Użycie

### Moduł Tworzenia Pliku .exe

Moduł tworzenia pliku .exe znajduje się w `src/exe_creator/creator.py`. Aby utworzyć plik .exe z kodu źródłowego Pythona, użyj poniższej komendy:

```bash
python src/exe_creator/creator.py path_to_your_script.py
```

### Moduł Crackowania Pliku .exe

Moduł crackowania pliku .exe znajduje się w `src/exe_cracker/cracker.py`. Aby rozpocząć analizę pliku .exe, użyj poniższej komendy:

```bash
python src/exe_cracker/cracker.py path_to_exe_file.exe
```

## Testowanie

Testy dla aplikacji znajdują się w katalogu `tests`. Aby uruchomić testy, użyj poniższej komendy:

```bash
pytest tests/
```

## Dokumentacja

Dokumentacja projektu znajduje się w katalogu `docs`. Plik `requirements.txt` zawiera listę wymaganych pakietów do zainstalowania.

## Tworzenie Struktury Katalogów

Jeżeli chcesz stworzyć strukturę katalogów dla projektu od podstaw, użyj skryptu PowerShell `create_structure.ps1`:

```powershell
.\create_structure.ps1
```

## Wkład

Jeżeli chcesz wnieść wkład w rozwój projektu, prosimy o stworzenie forka, a następnie wysłanie pull requesta z Twoimi zmianami. Prosimy również o dołączanie opisów wprowadzonych zmian oraz powiązanych problemów.

## Licencja

Projekt jest dostępny na licencji MIT. Więcej informacji w pliku `LICENSE`.

---

Dziękujemy za korzystanie z EducationalApp! Mamy nadzieję, że aplikacja ta pomoże Ci zrozumieć podstawy tworzenia oraz crackowania plików .exe.
