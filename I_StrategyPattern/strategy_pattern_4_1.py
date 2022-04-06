from typing import Protocol
from dataclasses import dataclass, field
import random

class I_ListClassifier(Protocol):
    def classify(self,lista:list):
        ...

    def print_init(self,lista:list) -> None:
        ...
#The 3 dots are a common way of ending protocol creations

#We encapsulate an specific behaviour (algorithm or concrete behaviour) in its own class
class RandomClassifier:
    def classify(self,lista:list) -> list:
        lista2 = lista.copy()
        random.shuffle(lista2)
        return lista2

    def print_init(self,lista:list) -> None:
        print(lista)

@dataclass
class InitialNumberClassifier:
    initial_index: int = 5 #Using the dataclass decorator we are avoinding to write the actual .__init__ method here
    def classify(self,lista:list) -> list:
        lista2 = lista[self.initial_index:].copy()
        lista2.extend(lista[:self.initial_index])
        return lista2

    def print_init(self,lista:list) -> None:
        print(lista)

@dataclass
class RemoveIndicesClassifier:
    revome_indices: list = field(default_factory=list)
    def classify(self,lista:list) -> list:
        lista2 = [el for i,el in enumerate(lista) if i not in self.revome_indices]
        return lista2

    def print_init(self,lista:list) -> None:
        print(lista)

#We create the client that uses the classification algorithm - And now decoupled from the specifics of each algorithm
class List_classifier:
    def __init__(self,lista:list,strategy: I_ListClassifier) -> None:
        self.lista = lista
        self.strat = strategy
    
    def classify_list(self):
        print(f'The provided classifier is {self.strat.__class__.__name__}')
        print(f'Given list {self.lista}')
        sorted_list = self.strat.classify(lista = self.lista)
        print(f'Classified list {sorted_list}')