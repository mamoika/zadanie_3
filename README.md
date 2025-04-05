# zadanie_3
# My Awesome Library

## Opis biblioteki
`My Awesome Library` to prosta biblioteka w Pythonie oferująca funkcje do operacji na plikach, obliczeń matematycznych oraz przetwarzania tekstu. Biblioteka została zaprojektowana jako przykład implementacji funkcji i testów jednostkowych.

## Funkcjonalności
### Operacje na plikach (`data_utils.py`)
- Odczyt danych z pliku (`read_file`).
- Zapis danych do pliku (`write_file`).

### Obliczenia matematyczne (`math_tools.py`)
- Dodawanie dwóch liczb (`add`).
- Mnożenie dwóch liczb (`multiply`).

### Przetwarzanie tekstu (`text_processing.py`)
- Liczenie słów w tekście (`count_words`).
- Odwracanie tekstu (`reverse_text`).

## Instrukcja instalacji
1. Sklonuj repozytorium:
git clone https://github.com/mamoika/zadanie_3.git   
cd zadanie_3
2. Zainstaluj bibliotekę lokalnie:
pip install -e .
## Przykłady użycia funkcji

### Operacje na plikach (`data_utils.py`)
rom my_awesome_lib.data_utils import read_file, write_file
write_file(“example.txt”, “Hello, World!”)
  
### Obliczenia matematyczne (`math_tools.py`)
print(read_file(“example.txt”))  # Output: Hello, World!

### Obliczenia matematyczne (`math_tools.py`)
from my_awesome_lib.math_tools import add, multiply
print(add(2, 3))        # Output: 5 
print(multiply(4, 5))   # Output: 20

### Przetwarzanie tekstu (`text_processing.py`)
from my_awesome_lib.text_processing import count_words, reverse_text
print(count_words(“Hello World”))  # Output: 2 print(reverse_text(“Python”))      # Output: nohtyP

## Informacje o autorze
- Autor: Ruslan Mamoika
- Wersja: 1.0.0  

