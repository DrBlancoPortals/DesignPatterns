import random

#Functional approach to the Strategy Pattern

def reversedClassifier_function(lista : list) -> list:
    lista2 = lista.copy()
    lista2.reverse()
    return lista2

def blackHoleClassifier_function(lista : list) -> list:
    return []

def randomClassifier_function(lista : list) -> list:
    lista2 = lista.copy()
    random.shuffle(lista2)
    return lista2

def sortingClassifier_function(lista:list) -> list:
    lista2 = lista.copy()
    lista2.sort()
    return lista2


class List_reader_functional:
    def __init__(self,lista:list) -> None:
        self.lista = lista
    
    def classify_list(self,strategy):
        print(f'The provided classifier is {strategy.__name__}')
        print(f'Given list {self.lista}')
        sorted_list = strategy(self.lista)
        print(f'Classified list {sorted_list}')


if __name__ == '__main__':
    lista = [1,4,7,0,12,5,43]
reader = List_reader_functional(lista)
reader.classify_list(randomClassifier_function)
reader.classify_list(reversedClassifier_function)
reader.classify_list(sortingClassifier_function)
reader.classify_list(blackHoleClassifier_function)