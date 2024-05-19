
# EducationalApp-CRACKER

EducationalApp-CRACKER to aplikacja dydaktyczna, która pomaga zrozumieć, jak tworzyć i crackować pliki wykonywalne, takie jak .exe, .net oraz .java. Dzięki tej aplikacji młodzi programiści mogą nauczyć się podstaw tworzenia plików wykonywalnych, zabezpieczania ich przed atakami oraz optymalizacji ich działania. 

## Struktura Katalogów

```
cracker/
├── EducationalApp-CRACKER/
│   ├── docs/
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   └── README.md
│   ├── src/
│   │   ├── doc_generator/
│   │   │   ├── __init__.py
│   │   │   └── README.md
│   │   ├── file_cracker/
│   │   │   ├── crackers/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── dotnet_cracker.py
│   │   │   │   └── general_cracker.py
│   │   ├── file_creator/
│   │   │   ├── generators/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── exe_generator.py
│   │   │   │   ├── java_generator.py
│   │   │   │   └── README.md
│   │   │   ├── utils/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── logger.py
│   │   │   └── __init__.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── README.md
│   │   └── main.py
│   ├── tests/
│   │   ├── test_cracker.py
│   │   ├── test_creator.py
│   │   ├── test_doc_generator.py
│   │   └── __init__.py
│   ├── LICENSE
│   └── main.py
├── venv/
├── .gitignore
└── README.md
```

## Funkcjonalności

EducationalApp-CRACKER oferuje następujące funkcje:

- **Tworzenie plików wykonywalnych**: Narzędzia do generowania plików .exe, .net i .java dla różnych platform i języków programowania.
- **Crackowanie plików**: Moduły do analizowania i łamania zabezpieczeń plików wykonywalnych.
- **Dokumentacja**: Automatyczne generowanie dokumentacji dla projektów.
- **Testowanie**: Zintegrowane testy jednostkowe do weryfikacji działania aplikacji.

## Instalacja

Aby zainstalować i uruchomić EducationalApp-CRACKER, wykonaj następujące kroki:

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/twoje-repo/EducationalApp-CRACKER.git
   ```

2. Przejdź do katalogu projektu:
   ```bash
   cd EducationalApp-CRACKER
   ```

3. Utwórz i aktywuj wirtualne środowisko:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Dla systemu Unix/macOS
   .\env\Scripts\ctivate    # Dla systemu Windows
   ```

4. Zainstaluj wymagane zależności:
   ```bash
   pip install -r docs/requirements.txt
   ```

5. Uruchom aplikację:
   ```bash
   python src/main.py
   ```

## Testowanie

Aby uruchomić testy, wykonaj następujące kroki:

1. Przejdź do katalogu projektu:
   ```bash
   cd EducationalApp-CRACKER
   ```

2. Uruchom testy:
   ```bash
   pytest tests/
   ```

## Konwencje Nazewnicze Commitów

Poniżej przedstawiono konwencje nazewnicze commitów stosowane w projekcie:

- **docs**: zmiany w dokumentacji
- **chore**: zmiany w narzędziach i konfiguracjach
- **feat**: dodanie nowej funkcjonalności
- **fix**: naprawa błędu
- **refactor**: refaktoryzacja kodu bez zmian w funkcjonalności
- **test**: dodanie lub modyfikacja testów
- **style**: zmiany w formatowaniu kodu, które nie wpływają na działanie (np. białe znaki, średniki)

### Przykłady Commitów

- `docs: budowa dokumentacji i aktualizacja README`
  - Dodano strukturę dokumentacji i zaktualizowano plik README.md w katalogu EducationalApp-CRACKER.
  - Commit zawiera następujące zmiany:
    - Utworzono katalog `docs` w `EducationalApp-CRACKER` z plikami:
      - `README.md`
      - `requirements.txt`
    - Zaktualizowano plik `README.md` w katalogu `EducationalApp-CRACKER/src/doc_generator`.
    - Dodano pliki `README.md` do odpowiednich katalogów w strukturze projektu.
  - Closes #13

- `docs: dodanie README.md do katalogu docs z konwencjami dokumentacyjnymi`
  - Dodano plik README.md do katalogu docs, w którym opisano konwencje dokumentacyjne projektu.
  - Commit zawiera następujące zmiany:
    - Utworzono plik `cracker/EducationalApp-CRACKER/docs/README.md` z opisem konwencji dokumentacyjnych.
  - Closes #14

- `chore: usunięcie pliku .gitignore`
  - Usunięto plik .gitignore z projektu.
  - Commit zawiera następujące zmiany:
    - Usunięto plik .gitignore z repozytorium.
  - Closes #12

- `feat: zmiana strony głównej`
  - Wprowadzono zmiany na stronie głównej, aby poprawić jej wygląd i funkcjonalność.
  - Commit zawiera następujące zmiany:
    - Aktualizacja układu strony głównej.
    - Dodanie nowych sekcji: "O nas", "Usługi" i "Kontakt".
    - Zmiana stylów CSS dla lepszej responsywności.
    - Optymalizacja obrazów dla szybszego ładowania strony.
    - Poprawa nawigacji i dodanie nowych linków w menu.
  - Closes #9


Aby zapewnić spójność i jakość kodu, stosujemy następujące konwencje dokumentowania:

- **Docstringi**: Używamy docstringów w formacie reStructuredText (reST) do dokumentowania funkcji, metod i klas.
- **Komentarze w kodzie**: Komentarze powinny być krótkie i rzeczowe, tłumaczące skomplikowane lub nietypowe fragmenty kodu.

### Przykład Docstringu

```python
def add(a, b):
    """
    Dodaje dwie liczby.

    :param a: Pierwsza liczba.
    :type a: int
    :param b: Druga liczba.
    :type b: int
    :return: Suma dwóch liczb.
    :rtype: int
    """
    return a + b
```

### Konfiguracja PyCharm dla Docstringów

1. **Ustawienia PyCharm**:
   - Przejdź do `File > Settings > Tools > Python Integrated Tools`.
   - W sekcji `Docstring format` wybierz `reStructuredText`.

2. **Generowanie Docstringów**:
   - Umieść kursor na funkcji lub metodzie.
   - Użyj skrótu `Alt + Enter` i wybierz `Insert documentation string stub`.

## Generowanie Dokumentacji

Aby wygenerować dokumentację projektu, używamy narzędzia Sphinx. Postępuj zgodnie z poniższymi krokami, aby wygenerować dokumentację:

1. Przejdź do katalogu `docs`:
   ```bash
   cd docs
   ```

2. Zainstaluj Sphinx:
   ```bash
   pip install sphinx
   ```

3. Inicjalizuj dokumentację Sphinx:
   ```bash
   sphinx-quickstart
   ```

4. Skonfiguruj plik `conf.py`, aby uwzględnić moduły projektu.

5. Wygeneruj dokumentację:
   ```bash
   make html
   ```

Wygenerowana dokumentacja będzie dostępna w katalogu `_build/html`.


