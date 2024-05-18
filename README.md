
# EducationalApp-CRACKER (REPO SET-UP)

EducationalApp-CRACKER to aplikacja dydaktyczna, która pomaga zrozumieć, jak tworzyć i crackować pliki wykonywalne (.exe). Dzięki tej aplikacji młodzi programiści mogą nauczyć się podstaw tworzenia plików .exe, zabezpieczania ich przed atakami oraz optymalizacji ich działania.

## Struktura Katalogów

```
cracker/
├── EducationalApp-CRACKER/
│   ├── docs/
│   │   ├── README.md
│   │   └── requirements.txt
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

## Opowieść o Super Krowie, Super Psie i Super Jeżu

```
          (__)
          (oo)
   /-------\/  
  / |     ||   
 *  ||----||      
    ^^    ^^      
  Super Krowa    

        /\_/\  
       ( o.o ) 
        > ^ <  
     Super Pies   
     
      ,,,  
     (o.o) 
     (   )  
    //| |\\   
  Super Jeż  
```

Dawno, dawno temu w cyfrowym królestwie mieszkała Super Krowa, Super Pies i ich nowy przyjaciel, Super Jeż. Razem postanowili stworzyć aplikację, która nauczy młodych programistów, jak tworzyć i crackować pliki .exe. Super Krowa, będąca mistrzynią tworzenia plików .exe, współpracowała z Super Psem, ekspertem od zabezpieczeń, a Super Jeż dołączył jako specjalista od optymalizacji i szyfrowania.

### Ich Misja

Super Krowa i Super Pies od lat pracowali nad rozwijaniem EducationalApp-CRACKER, ale czuli, że brakuje im kogoś z umiejętnościami Super Jeża. Ten mały, ale niezwykle bystry jeż miał dar do kodowania w niskopoziomowych językach i wiedział, jak maksymalnie zoptymalizować każde oprogramowanie.

Razem postanowili nie tylko nauczyć podstaw tworzenia plików .exe, ale także pokazać, jak można je zabezpieczyć przed różnymi atakami oraz jak je optymalizować, aby działały szybciej i były trudniejsze do złamania.

### Tworzenie EducationalApp-CRACKER

Super Krowa była odpowiedzialna za moduł `file_creator`, który generował różnego rodzaju pliki wykonywalne. W jej katalogu `src/file_creator/generators/` znajdowały się pliki takie jak `exe_generator.py` i `java_generator.py`, które były podstawą do tworzenia aplikacji.

Super Pies zajmował się modułem `file_cracker`, gdzie w katalogu `src/file_cracker/crackers/` znajdowały się pliki takie jak `dotnet_cracker.py` i `general_cracker.py`. Jego zadaniem było testowanie i crackowanie plików, aby młodzi programiści mogli zrozumieć, jak zabezpieczać swoje dzieła.

Super Jeż dodał do projektu moduł `utils`, w którym znajdowały się narzędzia do optymalizacji i szyfrowania. Jego `logger.py` w katalogu `src/file_creator/utils/` monitorował działanie aplikacji i zapewniał, że wszystko działało jak najlepiej.

### Razem Są Niepokonani

Dzięki wspólnej pracy, EducationalApp-CRACKER stała się niezwykle potężnym narzędziem dydaktycznym. Super Krowa, Super Pies i Super Jeż podróżowali po cyfrowym królestwie, ucząc młodych programistów, jak tworzyć, zabezpieczać i optymalizować swoje aplikacje. Ich misją było szerzenie wiedzy i przygotowanie nowych pokoleń programistów na wyzwania cyfrowego świata.

I tak, dzięki ich wspólnej sile i wiedzy, narodziła się aplikacja EducationalApp-CRACKER. Teraz każdy może nauczyć się sztuki tworzenia, crackowania i optymalizacji plików .exe, a także poznać tajniki zabezpieczeń cyfrowych.

## Więcej informacji

Więcej informacji znajdziesz w pełnym README.md!

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
   .\venv\Scripts\activate    # Dla systemu Windows
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

## Licencja

EducationalApp-CRACKER jest dostępny na licencji MIT. Zobacz plik `LICENSE` w katalogu głównym projektu, aby uzyskać więcej informacji.

---

Dziękujemy za korzystanie z EducationalApp-CRACKER! Mamy nadzieję, że nasza aplikacja będzie dla Ciebie wartościowym narzędziem edukacyjnym.
