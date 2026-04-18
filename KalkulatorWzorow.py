import math
co_obliczamy = int(input("""Podaj co obliczamy:
1. Podstawowe działania
2. Geometria – pola
0. Wyjście
 """))
if co_obliczamy == 1:
    print("Obliczamy podstawowe działania")
    dzialania_obliczamy = int(input("""Podaj co obliczamy:
1. Dodawanie
2. Odejmowanie
3. Mnożenie
4. Dzielenie
5. Potęgi
6. Pierwiastki
"""))
    if dzialania_obliczamy == 1:
        print("Dodajemy!")
        a = int(input("""Podaj pierwsza cyfre:"""))
        b = int(input("""Podaj druga cyfre:"""))
        wynik = a + b
        print(wynik)
    elif dzialania_obliczamy == 2:
        print("Odejmujemy!")
        a = int(input("""Podaj pierwsza cyfre:"""))
        b = int(input("""Podaj druga cyfre:"""))
        wynik = a - b
        print(wynik)
    elif dzialania_obliczamy == 3:
        print("Mnozymy!")
        a = int(input("""Podaj pierwsza cyfre:"""))
        b = int(input("""Podaj druga cyfre:"""))
        wynik = a * b
        print(wynik)
    elif dzialania_obliczamy == 4:
        print("Dzielimy!")
        a = int(input("""Podaj pierwsza cyfre:"""))
        b = int(input("""Podaj druga cyfre:"""))
        wynik = a / b
        print(wynik)
    elif dzialania_obliczamy == 5:
        print("Potegujemy!")
        a = int(input("""Podaj pierwsza cyfre:"""))
        b = int(input("""Podaj potege:"""))
        wynik = a ** b
        print(wynik)
    elif dzialania_obliczamy == 6:
        print("Pierwiastkujemy!")
        a = int(input("""Podaj cyfre:"""))
        wynik = math.sqrt(a)
        print(wynik)

if co_obliczamy == 2:
    print("Obliczamy Pola! ")
    pola_obliczamy = int(input("""Podaj co obliczamy:
1. Pole kwadratu
2. Pole prostokąta
3. Pole trójkąta
4. Pole trapezu
5. Pole równoległoboku
6. Pole koła
"""))

    if pola_obliczamy == 1:
        print("Obliczamy Pole Kwadratu! ")
        a = int(input(" Podaj a: "))
        wynik = a ** 2
        print(wynik)

    elif pola_obliczamy == 2:
        print("Obliczamy Pole Prostokata! ")
        a = int(input(" Podaj a: "))
        b = int(input(" Podaj b: "))
        wynik = a * b
        print(wynik)
    elif pola_obliczamy == 3:
        print("Obliczamy Pole Trojkata! ")
        a = int(input(" Podaj a: "))
        h = int(input(" Podaj h: "))
        wynik = (a * h) / 2
        print(wynik)

    elif pola_obliczamy == 4:
        print("Obliczamy Pole Trapezu! ")
        a = int(input(" Podaj a: "))
        b = int(input(" Podaj b: "))
        h = int(input(" Podaj h: "))
        wynik = ((a + b) * h) / 2
        print(wynik)
    elif pola_obliczamy == 5:
        print("Obliczamy Pole Równoległoboku ")
        a = int(input(" Podaj a: "))
        h = int(input(" Podaj h: "))
        wynik = a * h
        print(wynik)

    elif pola_obliczamy == 6:
        print("Obliczamy Pole Kola ")
        r = int(input(" Podaj promien: "))
        wynik = (r ** 2) * math.pi
        print(wynik)
