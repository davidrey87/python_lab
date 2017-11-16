# -*- coding: utf-8 -*-
from collections import OrderedDict

""" Repaso interactivo de python
"""


def lower_up(lower, upper):
    """ 1: Returns a list of numbers from the lower number to the upper number:
    >>> lower_up(5,15)
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    """
    for lower in range(lower, upper+1):
        print(lower)


def all_the_args(*args, **kwargs):
    """ 2: Return an array. Use * to expand positional args
    and use ** to expand keyword args
    >>> all_the_args(1, 2, a=3, b=4)
    (1, 2)
    {'a': 3, 'b': 4}
    """
    print(args)
    print(kwargs)


def may_20(tup):
    """ 3: Definir una tupla con 10 números.
    Imprimir la cantidad de números superiores a 20.
    >>> may_20((10, 16, 22, 26, 27, 30))
    22, 26, 27, 30
    """
    superiores = ""
    for x in tup:
        superiores = compara_20(superiores, x)

    print(superiores)


def compara_20(cadenaTMP, cadena):
    """ Comparamos si es mayor a 20
    """
    if cadena > 20:
        cadenaTMP = concatena_20(cadenaTMP, cadena)
    return cadenaTMP


def concatena_20(cadenaTMP, cadena):
    """ Concatenamos una cadena si esta o no vacia.
    """
    if cadenaTMP == "":
        cadenaTMP = str(cadena)
    else:
        cadenaTMP = cadenaTMP + ", " + str(cadena)
    return cadenaTMP


def word_filter(list_of_words, n):
    """ 4: Filtra las palabras que contienen más de n caracteres.
    >>> word_filter(['hello', 'bye', 'computer', 'software', 'python'], 5)
    ['computer', 'software', 'python']
    """
    a = 1
    for i in range(len(list_of_words)):
        if len(list_of_words[i-a]) <= n:
            list_of_words.remove(list_of_words[i-a])
            a = a + 1

    return list_of_words


def string_length(list):
    """ 5: imprime el largo de una cadena de caracteres
    >>> string_length("popularity")
    10
    """
    return len(list)


def is_vocal(x):
    """ 6: Determines if it is vocal
    >>> is_vocal('a')
    True
    >>> is_vocal('b')
    False
    """
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        return True
    else:
        return False


def is_leap_year(year):
    """ 7: Determines if a year is a leap year.
    >>> is_leap_year(2016)
    True
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


def has_uppercase(word):
    """ 8: Evaluate if a word has uppercase letters
    >>> has_uppercase('MayuSculA')
    3
    """
    count = 0
    for i in word.strip():
        if i.isupper():
            count = count + 1
    return count


def contar_vocales(cadena):
    """ 9: Return number of vocales in a word.
    >>> contar_vocales('murcielago')
    5
    """
    count = 0
    for i in cadena.strip():
        if is_vocal(i):
            count = count + 1
    return count


def square(list):
    """ 10: Calculate the square of the numbers in a list
    >>> l = [0, 1, 2, 3]
    >>> square(l)
    [0, 1, 4, 9]
    """
    temp = []
    for i in range(len(list)):
        temp.append(list[i]*list[i])

    print(temp)


def is_prime(n):
    """ 11:  Return if n is prime.
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    if n > 1:
        return is_prime_range(n)
    else:
        return False


def is_prime_range(n):
    """ Vemos si se da un resultado exacto 
    """
    for i in range(2, n):
        return is_prime_zero(n, i)


def is_prime_zero(n, i):
    """ Verificamos si se da un resultado exacto 
    """
    if (n % i) == 0:
        return False
        break
    else:
        return True
        break


def factorial(n):
    """ 12: Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(long(n)) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000L
    """
    if n == 0:
        return 1
    else:
        return int(n * factorial(n-1))


def to_roman(n):
    """ 13: Convert number integer to Roman numeral
    >>> to_roman(598)
    'DXCVIII'
    """
    return "".join([a for a in roman_num(n)])


def rima(word1, word2):
    """ 14: Indica si dos palabrar riman. Si coinciden las 3 ultimas letras rima,
    si ncoinciden solo 2 rima un poco, si coincide solo 1 no rima.
    >>> rima('flor', 'coliflor')
    rima
    >>> rima('amar', 'plantar')
    rima un poco
    >>> rima('azucar', 'barrer')
    no rima
    """
    x = "no rima"
    if word1[len(word1)-3:len(word1)] == word2[len(word2)-3:len(word2)]:
        x = "rima"
    elif word1[len(word1)-2:len(word1)] == word2[len(word2)-2:len(word2)]:
        x = "rima un poco"
    print(x)


def capital(pesos, interes, anios):
    """ 15: Pide una cantidad de pesos, una tasa de interés y un numero de años.
    Muestra en cuanto se habrá convertido el
    capital inicial transcurridos esos años si cada
    año se aplica la tasa de interés introducida.
    >>> capital(10000, 4.5, 20)
    24117.14
    """
    total = pesos*(1 + interes/100)**anios
    print("%.2f" % total)


def roman_num(n):
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"
    for r in roman.keys():
        x, y = divmod(n, r)
        yield roman[r] * x
        n -= (r * x)
        if n > 0:
            roman_num(n)
        else:
            break
