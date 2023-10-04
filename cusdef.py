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
