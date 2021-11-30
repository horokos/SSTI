# SSTI

## Jinja2

### Przygotowanie
- Do wykonania ćwiczeń będzie Ci potrzebny system (najlepiej Linux) z Python3.
- Pobierz repozytorium na swoją maszyne: `git clone https://github.com/horokos/SSTI`.
- Zainstaluj potrzebne moduły pythona: `pip install -r requirements.txt`. Jeśli nie masz pip: `sudo apt install python3-pip`.
- Uruchom aplikację: `python3 app.py` http://127.0.0.1:5000/.

### Zadanie 1
- Korzystając z [dokumentacji](https://jinja.palletsprojects.com/en/3.0.x/templates/), zapoznaj się ze składnią Jinjy2.
- Wykonaj proste wyrażenie arytmetyczne np.: `2+2`.

### Zadanie 2
- Zapoznaj się z budową aplikacji we Flasku: https://flask.palletsprojects.com/en/2.0.x/config/.
- Wypisz *config* aplikacji.

### Zadanie 3
- Korzystając z artykułów, ([\[1\]](https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/), [\[2\]](https://www.studytonight.com/python-howtos/how-to-find-all-the-subclasses-of-a-class-given-its-name)) zapoznaj się z dziedziczeniem klas w pythonie.
- Zapoznaj się także z klasą `subprocess`: https://docs.python.org/3/library/subprocess.html.
- Używając dziedziczenia klas i podklas, znajdź klasę `subprocess`. Wykorzystaj do tego np. `string( '' )`, `tuple( () )` lub `list( [] )` oraz metodę __`class`__.
- Wypisz pliki znajdujące się w folderze aplikacji.
- Dowiedz się, co znajduje się w tych plikach.
- Nadpisz wybrany plik.

### Zadanie 4
- Wyłącz aplikację zdalnie.

### Zadanie 
- Poszukaj w internecie, jak inaczej można dostać się do klasy `subprocess` lub jakiej innej klasy można użyć do wykonania tych ćwiczeń.

# Od tej części zadania będą wykonywane tylko w przeglądarce

 - Zadania będą widoczne na stronie https://194.36.88.83/. 
 - Prosimy o ustawienie prawdziwego imienia oraz nazwiska gdyż na tej podstawie będą przydzielane plusy

## Mako
 - Zapoznaj się z odpowiednim operatorem https://dmeg.tech/images/ssti.png.
 - Spróbuj wykonać proste dodanie do tekstu za pomocą komendy `.join()`.
 - Zaimportuj tę samą co w zadaniu wyżej komendę do pythona - [może pomóc ci w tym import](https://0x00sec.org/t/execute-system-commands-in-python-reference/7870).
 - Dokładnie przyjrzyj się co się znajduje koło aplikacji - może gdzieś tam jest flaga 👀.

## Pewna PHPowa templatka
- Zgadnij, jakiej templatki używa ta PHP-owa stronka.
- Spróbuj znaleźć, jakie komendy w PHP-ie są używane do wykonywania systemowych poleceń.
- Flaga jest odpowiednio zaszyfrowana - czy jesteś w stanie odgadnąć czym?

## Dla ambitnych zadanie: Jade. Ale gdzie?
- W poleceniu ukryta jest nazwa silnika templatek - proszę ją odszukać i sprawdzić, jaki język programowania wykorzystuje.
- Znajdź w *tym* języku analogiczne struktury do tych pythona.
- Za ich pomocą znajdź flagę.

## doT.js
- https://olado.github.io/doT/index.html
- Użyj analogicznej struktury jak w Jade żeby odnaleść flage

## Who am I
- Zgadnij, jak działa ta strona.
- Znajdź flagę.
