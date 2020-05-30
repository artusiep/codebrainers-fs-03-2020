## Dzień 2
### Powtórki
#### OOP
Jeżeli jeszcze nie doczytaliście o OOP to tutaj https://realpython.com/python3-object-oriented-programming/
### Zadanie
Napisz program przy pomocy klas który będzie rysował plansze do gry w kółko, krzyżyk na konsoli
Przykładowa plansza powinna wyglądać tak:
```
 | | 
-+-+-
 | |
-+-+-
 | |
```
metody jakie powinna zawierać klasa to:
* draw() - rysuje obecny stan planszy wraz z wypełnionymi polami np.
```
 | | 
-+-+-
 |X|
-+-+-
 | |O
``` 
* _put_char(char, x, y)
* put_x(x, y) - bądźmy mądrzy przy pisaniu tej metody 
* put_y(x, y) - bądźmy mądrzy przy pisaniu tej metody
* clean() - czyści planszę
Jakiej struktury danych użyjesz do przechowywania stanu planszy? przed przystąpieniem do implementacji skonsultuj to ze mną