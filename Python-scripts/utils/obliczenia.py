import math

def f1_abs(a):
    return print(f"Wartosc bezwględna z liczby {a} to:", math.fabs(a))

def f2_pow(a,b):
    return print(f"Potęga liczby {a} do potęgi {b} to:", math.pow(a, b))

def f3_sqrt(a):
    try:
        return print(f"Pierwiastek {a} to:", math.sqrt(a))
    except:
        return print(f"Pierwiastek {a}: Błąd! Liczba powinna być dodatnia")


def f4_sin(a):
    return print(f"Sinus {a} to:", math.sin(a))
