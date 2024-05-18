# EducationalApp-CRACKER

EducationalApp-CRACKER to aplikacja dydaktyczna mająca na celu naukę tworzenia i crackowania plików wykonywalnych (.exe) oraz plików Java (.jar). Aplikacja uczy także technik łamania zabezpieczeń plików .NET.

## Struktura Katalogów

```
/EducationalApp-CRACKER
├── /src
│   ├── /exe_creator
│   │   ├── /binary_generators
│   │   │   ├── exe_generator.py
│   │   │   ├── java_generator.py
│   │   ├── /crackers
│   │   │   ├── dotnet_cracker.py
│   │   │   ├── general_cracker.py
│   │   ├── /utils
│   │   │   ├── logger.py
│   │   └── __init__.py
│   ├── /exe_cracker
│   │   ├── cracker.py
│   │   └── __init__.py
│   ├── main.py
├── /tests
│   ├── test_creator.py
│   ├── test_cracker.py
├── /docs
│   ├── README.md
│   ├── requirements.txt
├── create_structure.ps1
├── LICENSE
└── README.md
```

## Instalacja

1. Sklonuj repozytorium:

   ```bash
   git clone https://github.com/DonkeyJJLove/EducationalApp-CRACKER.git
   ```

2. Przejdź do katalogu projektu:

   ```bash
   cd EducationalApp-CRACKER
   ```

3. Utwórz wirtualne środowisko:

   ```bash
   python -m venv venv
   ```

4. Aktywuj wirtualne środowisko:

   - Windows:

     ```bash
     .\venv\Scripts\activate
     ```

5. Zainstaluj wymagane pakiety:

   ```bash
   pip install -r docs/requirements.txt
   ```

## Użycie

### Moduł Tworzenia Pliku .exe

Aby utworzyć plik .exe z kodu źródłowego Pythona:

```bash
python src/exe_creator/binary_generators/exe_generator.py path_to_your_script.py --output path_to_output.exe
```

### Moduł Tworzenia Pliku .jar

Aby utworzyć plik .jar z kodu źródłowego Java:

```bash
python src/exe_creator/binary_generators/java_generator.py path_to_your_script.java --output path_to_output.jar
```

### Moduł Crackowania Pliku .NET

Aby crackować plik .NET:

```bash
python src/exe_creator/crackers/dotnet_cracker.py path_to_exe_file.exe
```

### Moduł Crackowania Ogólnego Pliku Wykonywalnego

Aby crackować ogólny plik wykonywalny:

```bash
python src/exe_creator/crackers/general_cracker.py path_to_exe_file.exe
```

### Logowanie

Logi są zapisywane w plikach logów w katalogu projektu. Każdy submoduł ma swój własny plik logów, co umożliwia łatwą analizę.

### Użycie Pliku `main.py`

Plik `main.py` umożliwia uruchamianie różnych trybów pracy aplikacji. Przykładowe użycie:

```bash
python src/main.py --mode generate_exe --input path_to_your_script.py --output path_to_output.exe
python src/main.py --mode generate_jar --input path_to_your_script.java --output path_to_output.jar
python src/main.py --mode crack_dotnet --input path_to_exe_file.exe
python src/main.py --mode crack_general --input path_to_exe_file.exe
```

## Testowanie

Aby uruchomić testy:

```bash
pytest tests/
```

## Licencja

Projekt jest dostępny na licencji MIT. Więcej informacji w pliku `LICENSE`.

---

Dziękujemy za korzystanie z EducationalApp-CRACKER! Mamy nadzieję, że aplikacja ta pomoże Ci zrozumieć podstawy tworzenia oraz crackowania plików .exe i .jar oraz technik łamania zabezpieczeń plików .NET.