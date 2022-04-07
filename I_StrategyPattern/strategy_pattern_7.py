import random
from typing import Callable,Optional
from dataclasses import dataclass, field

# Functional approach to the Strategy Pattern - Part III -> 
# Creating aliases with Callable
# And using Closures for extra arguments

# Let us assume that we want to be able to add extra arguments which are 
# different for each strategy, and work our way around the limitations 
# of the Callable rigidity. We can resort to closures


I_ListClassifier = Callable[[list],list]

def reversedClassifier_function(lista : list) -> list:
    lista2 = lista.copy()
    lista2.reverse()
    return lista2

def blackHoleClassifier_function(lista : list) -> list:
    return []

#Now, the random method will be defined by a closure, so 
#we can add the seed for the classifier
def randomClassifier_function_creator(seed: Optional[int]) -> I_ListClassifier:
    def randomClassifier_function(lista : list) -> list:
        lista2 = lista.copy()
        random.seed(seed)
        random.shuffle(lista2)
        return lista2
    return randomClassifier_function

def sortingClassifier_function(lista:list) -> list:
    lista2 = lista.copy()
    lista2.sort()
    return lista2


# Given that the alias of Callable does not distinguish between actual functions ç
# and classes with __call__ methods, we can mix both

@dataclass
class RemoveIndicesClassifier:
    revome_indices: list = field(default_factory=list)
    def __post_init__(self):
        """The post_init method ensures the creating of the __name__ variable,
        as it is a requirement by the Client side of things"""
        self.__name__ = 'RemoveIndicicesClassifier'
    def __call__(self,lista:list) -> list:
        lista2 = [el for i,el in enumerate(lista) if i not in self.revome_indices]
        return lista2


# And as always, the client side of things


class List_reader_functional:
    def __init__(self,lista:list,strategy:I_ListClassifier) -> None:
        self.lista = lista
        self.strategy = strategy
    
    def classify_list(self):
        print(f'The provided classifier is {self.strategy.__name__}')
        print(f'Given list {self.lista}')
        sorted_list = self.strategy(self.lista)
        print(f'Classified list {sorted_list}')


if __name__ == '__main__':
    lista = [1,4,7,0,12,5,43]
    reader = List_reader_functional(lista,strategy=randomClassifier_function_creator(seed=2))
    reader.classify_list()
    reader = List_reader_functional(lista,strategy=blackHoleClassifier_function)
    reader.classify_list()
    reader = List_reader_functional(lista,strategy=reversedClassifier_function)
    reader.classify_list()
    reader = List_reader_functional(lista,strategy=sortingClassifier_function)
    reader.classify_list()
    #Let's see if the class works
    reader = List_reader_functional(lista,strategy=RemoveIndicesClassifier(revome_indices=[0,1,4]))
    reader.classify_list()
    #And using another seed for the random classifier case
    reader = List_reader_functional(lista,strategy=randomClassifier_function_creator(seed=25))
    reader.classify_list()