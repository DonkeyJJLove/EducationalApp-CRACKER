### generators

- `exe_generator.py`: Generuje pliki .exe z kodu źródłowego Pythona.
- `java_generator.py`: Generuje pliki .jar z kodu źródłowego Java.

### utils

- `logger.py`: Ustawia logger dla aplikacji.

## Instalacja i Użycie

1. Aby utworzyć plik .exe z kodu źródłowego Pythona:

    ```bash
    python src/file_creator/generators/exe_generator.py path_to_your_script.py --output path_to_output.exe
    ```

2. Aby utworzyć plik .jar z kodu źródłowego Java:

    ```bash
    python src/file_creator/generators/java_generator.py path_to_your_script.java --output path_to_output.jar
    ```

