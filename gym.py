"""
[sumary]

Args: 
    n1 (Int): [description] 
    n2 (Int): [description] 
Returns: 
    [type]:[description]
"""


# ----------------------------------------------------------------------------------------#

from os import remove


def maximo3(n1: int, n2: int, n3: int):
    """
[Compara 3 numeros y devuelve el mayor]

Args: 
    n1 (Int): [Valor a comparar 1] 
    n2 (Int): [Valor a comparar 2]
    n3 (int): [Valor a comparar 3] 
Returns: 
    [Int]:[El mayor numero ingresado]

    <<< maximo3(1,2,3)
    3 
    <<< maximo3(1,2,33)                              #python3 -m doctest archivo.py
    33
    """
    n = max(n1, n2)
    n_final = max(n, n3)
    if n == n_final:
        return "Son iguales"
    return n_final


# print(maximo3(3, 3, 3))

# ------------------------------------------------------------------------#


def simpleArraySum(ar):
    """
    Description: 
    Devuelve la suma de una lista ingresada]

    Args: 
    ar : lista ó tupla

    Returns: 
    suma de la lista
    """
    n1 = 0
    for numero in ar:
        n1 += numero

    return n1


#print(simpleArraySum([1,2,-1]))

# ------------------------------------------------------------------------#


def compareTriplets(a, b):
    # Write your code here
    alice = bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return alice, bob


# ------------------------------------------------------------------------#


def diagonalDifference(arr):
    for d in arr:
        return abs((d[0][0] + d[1][1] + d[2][2]) - ((d[0][2] + d[1][1] + d[2][0])))


matriz1 = [11, 2, 4]
matriz2 = [4, 5, 6]
matriz3 = [10, 8, -12]
matrizz = [matriz1, matriz2, matriz3]


# print(diagonalDifference([matrizz]))


#------------------------------------------------------------------------#


def sinrep(arr : list):
    """
    Description: 
    Devuelve una lista sin repeticiones de numeros

    Args: 
    Una lista 

    Returns: 
    Lista sin repeticiones
    """
    arrAux = set()   # Recordar funcion ser()
    for element in arr:
        arrAux.add(element)
    return list(arrAux)


#print(sinrep([1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 9]))

#------------------------------------------------------------------------#

#Sintaxis recursiva que usaba en Haskell 
def sum(lista : list) -> int:
  if len(lista) == 0:
      return 0 
  else: 
      return lista[0] + sum(lista[1:])            

#print(sum([2,2,1]))

#------------------------------------------------------------------------#

#  card: [Int] → Int, que dada una lista devuelve la cantidad de elementos de la lista.


def card(arr : list) -> int: 
    if len(arr) == 0:
        return 0 
    else:
        return 1 + card(arr[1:])

#print(card([2,2,1]))

#------------------------------------------------------------------------#

#multiply [int] -> int que multiplica entre si los elementos de una lista 

def multiply(arr: list) -> int: 
    if len(arr) == 0:  
        return 1 
    else: 
       return arr[0] * multiply(arr[1:])    

#print(multiply([2,2,1]))

#------------------------------------------------------------------------#

# todosMenores10: [Int] → Bool, que dada una lista devuelve True si ésta consiste sólo de 
# números menores que 10 y False en caso contrario.

def menores10(arr: list) -> bool: 
    if len(arr) == 0: 
        return True
    else: 
       return arr[0] < 10 and menores10(arr[1:])   

#print(menores10([2,2,1]))  

#------------------------------------------------------------------------#

#sumar1: [Int] → [Int], que dada una lista de enteros le suma uno a cada uno de sus elementos.
#  Por ejemplo: sumar1.[3, 0, −2] = [4, 1, −1]

def sumar1(arr):
  return list(map(lambda args: args + 1, arr))

#print(sumar1([2,2,1]))    

#------------------------------------------------------------------------#

#Funcion que devuelva inversa de una cadena. Por ejemplo "jugar" = "raguj"

def inversa(cadena):  
    return cadena[::-1]

#print(inversa("amor"))   

#------------------------------------------------------------------------#

#Escriba una función que acepte una matriz de 10 enteros (entre 0 y 9),
#  que devuelva una cadena de esos números en forma de número de teléfono.


def create_phone_number(n: list):
 return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"


#------------------------------------------------------------------------#
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


#print(alphabet_position("abcd"))

#------------------------------------------------------------------------#

#You are going to be given a word. Your job is to return the middle character of the word.
#  If the word's length is odd, return the middle character.
#  If the word's length is even, return the middle 2 characters.

def get_middle(text):
    n = len(text)
    if n % 2 == 0:
        return text[int(n/2-1):int(n/2 + 1)]
    else:
        return text[int(n/2)]

#print(get_middle("negraso"))        

    

#------------------------------------------------------------------------#

#Complete the method/function so that it converts dash/underscore delimited words into camel casing.
#  The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case).

def to_camel_case(text):
    if "_"  in text: 
        return text.sub("_")

print(to_camel_case("alexis_martens"))        
