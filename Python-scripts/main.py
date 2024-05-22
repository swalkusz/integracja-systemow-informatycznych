import math
import random
import string

def skrypt1():
    print("Zad 1: ")
    a = input("wpisz znak: ")
    if len(a) > 1:
        return print("To jest ciąg znaków - nie jest cyfrą")
    elif len(a) == 0:
        return print("Brak wpisanego znaku! ")
    # pierwszy sposób
    if a.isdigit():
        print("f. isdigit(): Jest cyfrą")
    else:
        print("f. isdigit(): Nie jest cyfrą")

    # drugi sposób
    try:
        a = int(a)
    except:
        pass
    if isinstance(a, (int, complex, float)):
        print("f. isinstance(): Jest cyfrą")
    else:
        print("f. isinstance(): Nie jest cyfrą")


def skrypt2():
    print("Zad 2: ")
    a = input("wpisz ciąg znaków: ")
    if len(a) < 2:
        return print("Ciąg znaków jest za krótki! Wpisz min 2 znaki! ")
    if a.isdigit():
        print("Jest liczbą")
    else:
        print("Nie jest liczbą")


def skrypt3():
    print("Zad 3: ")
    a = input("wpisz ciąg znaków: ")
    if len(a) == 0:
        return print("Ciąg jest pusty!")
    b = input("wpisz szukaną sekwencję znaków: ")
    if len(a) == 0:
        return print("Ciąg jest pusty!")
    print(a.find(b))


def skrypt4():
    print("Zad 4: ")
    a = input("wpisz ciąg znaków: ")
    if len(a) == 0:
        return print("Ciąg jest pusty!")
    b = input("wpisz szukaną sekwencję znaków: ")
    if len(a) == 0:
        return print("Ciąg jest pusty!")
    for x in b:
        print("index dla " ,x , ": " , a.find(x))


def skrypt5():
    print("Zad 5: ")
    # pierwszy sposób
    for i in range(1, 257):
        if i % 2 == 0:
            print("Pierwiastek z ",i," = ",math.sqrt(i))
    # drugi sposób
    print([math.sqrt(i) for i in range(1, 257) if i % 2 == 0])


def skrypt6():
    print("Zad 6: ")
    # print(''.join(random.choices(string.ascii_letters, k=8)))
    def genPseudoStr(dlugosc):
        return ''.join(random.choices(string.ascii_letters, k=dlugosc))

    slownik24012  = dict()
    for i in range(10,21):
        slownik24012[i] = genPseudoStr(8)

    for key,value in slownik24012.items():
        print(f"{key} - {value}")

    print(f"Moj słownik to: {slownik24012}")


def skrypt7():
    print("Zad 7")
    from utils.obliczenia import f1_abs,f2_pow,f3_sqrt,f4_sin
    a = -20
    b = 3
    f1_abs(a)
    f2_pow(a,b)
    f3_sqrt(a)
    f4_sin(a)


def skrypt8():
    print("Zad 8")
    print("Zliczanie znaków")
    from collections import Counter
    def genPseudoStr(dlugosc):
        return ''.join(random.choices(string.ascii_letters, k=dlugosc))
    def occourences(text):
        myDict = Counter(text)
        acc = []
        for key, value in myDict.items():
            acc.append((key,value))
        return acc

    text_value = genPseudoStr(100)
    wynik = occourences(text_value)
    for index, liczba_wystopien in enumerate(wynik):
        print(f"{index + 1}: {liczba_wystopien}")


def skrypt9():
    print("Zad 9")
    class Vehicle:
        def __init__(self, nazwa, rokprod, przebieg):
            self.nazwa = nazwa
            self.rokprod = rokprod
            self.przebieg = przebieg

        @property
        def is_long_mileage(self):
            return self.przebieg > 100000

        @property
        def is_old(self):
            return self.rokprod < 2000

    class Car:
        def __init__(self, nazwa, rokprod, przebieg):
            self.nazwa = nazwa
            self.rokprod = rokprod
            self.przebieg = przebieg

        @property # dzieli temu wywołujemy be nawiasów
        def is_long_mileage(self):
            return self.przebieg > 100000

        @property
        def is_old(self):
            return self.rokprod < 2000

    class Third(Car, Vehicle): # dziedziczy z tych 2 klas
        pass

    v1 = Vehicle("volvo", 2009, 220000)
    c1 = Car("volvo", 2014, 220000)
    t1 = Third("volvo", 1999, 220000)
    print(v1.is_old)
    print(v1.is_long_mileage)
    print(c1.is_old)
    print(c1.is_long_mileage)
    print(t1.is_old)
    print(t1.is_long_mileage)


def skrypt10():
    print("Zad 10")
    letters = []

    for i in range (65 ,91):
        letters.append(chr(i))
    lettersStr = ''.join(letters)
    print(lettersStr)
    with open("alfabet1-24012.txt", "w") as file:
            file.write(lettersStr)

    with open("alfabet2-24012.txt", "w") as file:
        for letter in lettersStr:
            file.write(f"{letter}\n")

# Można wywoływać poszczególne funkcje
if __name__ == '__main__':
    skrypt1()
    skrypt2()
    skrypt3()
    skrypt4()
    skrypt5()
    skrypt6()
    skrypt7()
    skrypt8()
    skrypt9()
    skrypt10()