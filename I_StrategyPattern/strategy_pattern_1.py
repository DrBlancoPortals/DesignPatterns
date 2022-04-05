from abc import ABC, abstractmethod
import random

#OOP approach (pure) to the Strategy Pattern

class I_NumClassifier(ABC):
    @abstractmethod
    def classify(self,*args,**kwargs):
        pass

class RandomClassifier(I_NumClassifier):
    def classify(self,lista:list) -> list:
        lista2 = lista.copy()
        random.shuffle(lista2)
        return lista2

class ReversedClassifier(I_NumClassifier):
    def classify(self,lista:list) -> list:
        lista2 = lista.copy()
        lista2.reverse()
        return lista2

class SortingClassifier(I_NumClassifier):
    def classify(self,lista:list) -> list:
        lista2 = lista.copy()
        lista2.sort()
        return lista2


class BlackHoleClassifier(I_NumClassifier):
    def classify(self,lista:list) -> list:
        return []



class List_reader:
    def __init__(self,lista:list) -> None:
        self.lista = lista
    
    def classify_list(self,strategy: I_NumClassifier):
        print(f'Used Strategy : {strategy().__class__.__name__}')
        print(f'Given list {self.lista}')
        sorted_list = strategy().classify(self.lista)
        print(f'Classified list {sorted_list}')


if __name__ == '__main__':
    lista = [1,4,7,0,12,5,43]
    reader = List_reader(lista)
    reader.classify_list(RandomClassifier)
    reader.classify_list(ReversedClassifier)
    reader.classify_list(SortingClassifier)
    reader.classify_list(BlackHoleClassifier)
    