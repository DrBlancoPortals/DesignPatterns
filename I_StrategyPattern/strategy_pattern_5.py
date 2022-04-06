from typing import Protocol
from dataclasses import dataclass, field
import random
#Using protocols, but making use of the __call__ to avoind problems with the typing 
# somewhere else down the line (in other potential sripts)

#We create the abstract class for the classification method
class I_ListClassifier(Protocol):
    def __call__(self,lista:list):
        ...
#The 3 dots are a common way of ending protocol creations

#We encapsulate an specific behaviour (algorithm or concrete behaviour) in its own class
class RandomClassifier:
    def __call__(self,lista:list) -> list:
        lista2 = lista.copy()
        random.shuffle(lista2)
        return lista2

@dataclass
class InitialNumberClassifier:
    initial_index: int = 5 #Using the dataclass decorator we are avoinding to write the actual .__init__ method here
    def __call__(self,lista:list) -> list:
        lista2 = lista[self.initial_index:].copy()
        lista2.extend(lista[:self.initial_index])
        return lista2

@dataclass
class RemoveIndicesClassifier:
    revome_indices: list = field(default_factory=list)
    def __call__(self,lista:list) -> list:
        lista2 = [el for i,el in enumerate(lista) if i not in self.revome_indices]
        return lista2

#We create the client that uses the classification algorithm - And now decoupled from the specifics of each algorithm
class List_classifier:
    def __init__(self,lista:list,strategy: I_ListClassifier) -> None:
        self.lista = lista
        self.strat = strategy
    
    def classify_list(self):
        print(f'The provided classifier is {self.strat.__class__.__name__}')
        print(f'Given list {self.lista}')
        sorted_list = self.strat(lista = self.lista)
        print(f'Classified list {sorted_list}')


if __name__ == '__main__':
    lista = [1,4,7,0,12,5,43]
    reader = List_classifier(lista,InitialNumberClassifier(initial_index=2))
    reader.classify_list()

    reader = List_classifier(lista,RandomClassifier())
    reader.classify_list()

    reader = List_classifier(lista,RemoveIndicesClassifier(revome_indices=[0,1,4]))
    reader.classify_list()