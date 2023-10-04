# Funciones personalizadas
from os import system as osystem

def cls() -> None:
    '''Clear console'''
    osystem('clear')

def dideco(text:str) -> str:
    '''Invierte las palabras sin cambiar su orden dentro de la oracion'''
    return " ".join([i[::-1] for i in text.split(" ")])

def intext(text:str) -> str:
    '''Invierte una oracion'''
    return text[::-1]

def palincheck(input_string:str) -> bool:
    return input_string.lower()[::-1] == input_string.lower()

def ordanilist(my_list:list) -> list:
    new_list = [i for element in my_list for i in element]
    new_list.sort(reverse=True)
    return new_list
