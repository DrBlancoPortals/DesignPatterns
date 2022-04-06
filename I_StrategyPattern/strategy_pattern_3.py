from dataclasses import dataclass,field
from abc import ABC, abstractmethod
import random

#We create the abstract class for the classification method
class I_ListClassifier(ABC):
    @abstractmethod
    def classify(self,lista:list):
        pass

#We encapsulate an specific behaviour (algorithm or concrete behaviour) in its own class
class RandomClassifier(I_ListClassifier):
    def classify(self,lista:list) -> list:
        lista2 = lista.copy()
        random.shuffle(lista2)
        return lista2

@dataclass
class InitialNumberClassifier(I_ListClassifier):
    initial_index: int = 5 #Using the dataclass decorator we are avoinding to write the actual .__init__ method here
    def classify(self,lista:list) -> list:
        lista2 = lista[self.initial_index:].copy()
        lista2.extend(lista[:self.initial_index])
        return lista2

@dataclass
class RemoveIndicesClassifier(I_ListClassifier):
    revome_indices: list = field(default_factory=list)
    def classify(self,lista:list) -> list:
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
        sorted_list = self.strat.classify(lista = self.lista)
        print(f'Classified list {sorted_list}')




if __name__ == '__main__':
    lista = [1,4,7,0,12,5,43]
    reader = List_classifier(lista,InitialNumberClassifier(initial_index=2))
    reader.classify_list()

    reader = List_classifier(lista,RandomClassifier())
    reader.classify_list()

    reader = List_classifier(lista,RemoveIndicesClassifier(revome_indices=[0,1,4]))
    reader.classify_list()