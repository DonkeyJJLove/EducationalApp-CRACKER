
# Moduł exe_creator

Moduł `exe_creator` jest odpowiedzialny za generowanie plików wykonywalnych oraz crackowanie zabezpieczeń. W skład modułu wchodzą trzy główne submoduły:

1. `binary_generators`: Służy do generowania plików binarnych (.exe, .jar).
2. `crackers`: Służy do łamania zabezpieczeń plików wykonywalnych, w tym plików .NET.
3. `utils`: Zawiera narzędzia wspomagające, takie jak logger.

## Struktura Katalogów

```
/exe_creator
├── /binary_generators
│   ├── exe_generator.py
│   ├── java_generator.py
├── /crackers
│   ├── dotnet_cracker.py
│   ├── general_cracker.py
├── /utils
│   ├── logger.py
└── __init__.py
```

### binary_generators

- `exe_generator.py`: Generuje pliki .exe z kodu źródłowego Pythona.
- `java_generator.py`: Generuje pliki .jar z kodu źródłowego Java.

### crackers

- `dotnet_cracker.py`: Crackuje pliki .NET.
- `general_cracker.py`: Crackuje ogólne pliki wykonywalne.

### utils

- `logger.py`: Ustawia logger dla aplikacji.

## Instalacja i Użycie

1. Aby utworzyć plik .exe z kodu źródłowego Pythona:

    ```bash
    python src/exe_creator/binary_generators/exe_generator.py path_to_your_script.py
    ```

2. Aby utworzyć plik .jar z kodu źródłowego Java:

    ```bash
    python src/exe_creator/binary_generators/java_generator.py path_to_your_script.java
    ```

3. Aby crackować plik .NET:

    ```bash
    python src/exe_creator/crackers/dotnet_cracker.py path_to_exe_file.exe
    ```

## Logowanie

Logi są zapisywane w plikach logów w katalogu projektu. Każdy submoduł ma swój własny plik logów, co umożliwia łatwą analizę.
