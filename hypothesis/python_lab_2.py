# -*- coding: utf-8 -*-
from typing import List
from typing import Tuple
from math import sqrt
from contracts import contract
from itertools import count, islice
import calendar

""" Repaso interactivo de python
"""


@contract(lower='int,>0', upper='int,>0', returns=None)
def lower_up(lower: int, upper: int) -> None:
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
    for lower in range(lower, upper + 1):
        print(lower)


@contract(lower='int,>0', upper='int,>0', returns=None)
def lower_up_while(lower, upper):
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
    while(lower<upper+1):
        print(lower)
        lower += 1


@contract(args='tuple[N],N>0', kwargs='dict(str: (int))', returns=None)
def all_the_args(*args: str, **kwargs: str) -> None:
    """ 2: Return an array. Use * to expand positional args
    and use ** to expand keyword args
    >>> all_the_args(1, 2, a=3, b=4)
    (1, 2)
    {'a': 3, 'b': 4}
    """
    print(args)
    print(kwargs)


@contract(tup='tuple[N],N>0', returns=None)
def may_20(tup: Tuple[int]) -> None:
    """ 3: Definir una tupla con 10 números.
    Imprimir la cantidad de números superiores a 20.
    >>> may_20((10, 16, 22, 26, 27, 30))
    22, 26, 27, 30
    """
    superiores = ""
    for x in tup:
        superiores = compara_20(superiores, x)

    print(superiores)


@contract(cadenaTMP='str', cadena='int,>0', returns='str')
def compara_20(cadenaTMP: str, cadena: int) -> str:
    """ Comparamos si es mayor a 20
    """
    if cadena > 20:
        cadenaTMP = concatena_20(cadenaTMP, cadena)
    return cadenaTMP


@contract(word='str', returns=None)
def has_uppercase(word: str) -> None:
    """ 8: Evaluate if a word has uppercase letters
    >>> has_uppercase('MayuSculA')
    3
    """
    u = [x for x in word if x.isupper()]
    print(len(u))


@contract(cadenaTMP='str', cadena='int,>0', returns='str')
def concatena_20(cadenaTMP: str, cadena: int) -> str:
    """ Concatenamos una cadena si esta o no vacia.
    """
    if cadenaTMP == "":
        cadenaTMP = str(cadena)
    else:
        cadenaTMP = cadenaTMP + ", " + str(cadena)
    return cadenaTMP


@contract(list_='list(str)', n='int,>0', returns='list(str)')
def word_filter(list_: List[str], n: int) -> List[str]:
    """ 4: Filtra las palabras que contienen más de n caracteres.
    >>> word_filter(['hello', 'bye', 'computer', 'software', 'python'], 5)
    ['computer', 'software', 'python']
    """
    a = 1
    for i in range(len(list_)):
        list_ = word_list(list_, n, a, i)
        a = word_accepted(list_, n, a, i)
    return list_


@contract(li='list(str)', n='int,>0', a='int,>0', i='int', returns='list(str)')
def word_list(li: List[str], n: int, a: int, i: int) -> List[str]:
    if len(li[i-a]) <= n:
        li.remove(li[i-a])
    return li


@contract(list_='list(str)', n='int,>0', a='int,>0', i='int', returns='int')
def word_accepted(list_: List[str], n: int, a: int, i: int) -> int:
    if len(list_[i-a]) <= n:
        a = a + 1
    return a


@contract(list_='list(str)', n='int,>0', returns='list(str)')
def word_filter_2(list_, n):
    """ 4: Filtra las palabras que contienen más de n caracteres
    >>> word_filter(['hello', 'bye', 'computer', 'software', 'python'],5)
    ['computer', 'software', 'python']
    """
    lista = []
    for item in list_:
        if len(x) > n:
            lista.append(x)
    return(lista)


@contract(list='str', returns='int')
def string_length(list: str) -> int:
    """ 5: imprime el largo de una cadena de caracteres
    >>> string_length("popularity")
    10
    """
    return len(list)


@contract(x='str', returns='bool')
def is_vocal(x: str) -> bool:
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


@contract(year='int', returns=None)
def is_leap_year(year: int) -> None:
    """ 7: Determines if a year is a leap year.
    >>> is_leap_year(2016)
    True
    """
    print(calendar.isleap(year))


@contract(cadena='str', returns='int')
def contar_vocales(cadena: str) -> int:
    """ 9: Return number of vocales in a word.
    >>> contar_vocales('murcielago')
    5
    """
    count = 0
    for i in cadena.strip():
        count = separa_vocal(i) + count
    return count


@contract(i='str', returns='int')
def separa_vocal(i: str) -> int:
    if is_vocal(i):
        return 1
    return 0


@contract(list='list(int)', returns=None)
def square(list: List[int]) -> None:
    """ 10: Calculate the square of the numbers in a list
    >>> l = [0, 1, 2, 3]
    >>> square(l)
    [0, 1, 4, 9]
    """
    temp = []
    for i in range(len(list)):
        temp.append(list[i]*list[i])

    print(temp)


@contract(n='int', returns='bool')
def is_prime(n: int) -> bool:
    """ 11:  Return if n is prime.
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


@contract(n='int', returns='int')
def factorial(n: int) -> int:
    """ 12: Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(int(n)) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    """
    if n == 0:
        return 1
    else:
        return int(n * factorial(n-1))


@contract(n='int', returns='list(str)')
def to_roman(n: int) -> List[str]:
    """ 13: Convert number integer to Roman numeral
    >>> to_roman(598)
    ['DXCVIII']
    """
    val = (1000, 900,  500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    syb = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX',
           'V', 'IV', 'I')
    roman_num = ""
    list = []
    for i in range(len(val)):
        count = int(n / val[i])
        roman_num += syb[i] * count
        n -= val[i] * count
    list.append(roman_num)
    return list


@contract(word1='str', word2='str', returns=None)
def rima(word1: str, word2: str) -> None:
    """ 14: Indica si dos palabrar riman. Si coinciden las 3 ultimas letras rima,
    si ncoinciden solo 2 rima un poco, si coincide solo 1 no rima.
    >>> rima('flor', 'coliflor')
    rima
    >>> rima('amar', 'plantar')
    rima un poco
    >>> rima('azucar', 'barrer')
    no rima
    """
    x = ""
    x = rima_comparation(word1, word2, 2)
    if x == "rima un poco":
        x = rima_comparation2(word1, word2, 3)
    print(x)


@contract(word1='str', word2='str', n='int', returns='str')
def rima_comparation(word1: str, word2: str, n: int) -> str:
    if word1[len(word1)-n:len(word1)] == word2[len(word2)-n:len(word2)]:
        return "rima un poco"
    return "no rima"


@contract(word1='str', word2='str', n='int', returns='str')
def rima_comparation2(word1: str, word2: str, n: int) -> str:
    if word1[len(word1)-n:len(word1)] == word2[len(word2)-n:len(word2)]:
        return "rima"
    return "rima un poco"


@contract(pesos='float', interes='float', anios='float', returns=None)
def capital(pesos: float, interes: float, anios: float) -> None:
    """ 15: Pide una cantidad de pesos, una tasa de interés y un numero de años.
    Muestra en cuanto se habrá convertido el
    capital inicial transcurridos esos años si cada
    año se aplica la tasa de interés introducida.
    >>> capital(10000.00, 4.50, 20.00)
    24117.14
    """
    total = pesos*(1 + interes/100)**anios
    print("%.2f" % total)
