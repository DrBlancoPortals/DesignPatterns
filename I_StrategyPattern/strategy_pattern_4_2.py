from strategy_pattern_4_1 import List_classifier
'''
The awesome thing of using protocols in strategy_pattern_4_1 is that we no longer need
to import the abstract class here. So we can code directly classifier classes by following
the protocol stablished elsewhere ... 

Furthermore, if we would be only interested in some of several methods included in the
protocol, we no longer need to implement the rest of them. We are reducing the 
dependencies required...
'''
class BlackHoleClassifier:
    def classify(self,lista:list) -> list:
        return []
#Here, we didn't code the print_init, because is not needed 
#(well, we actually decide not to do it out of convenience)

def main():
    lista = [1,2,34,6,4,240,7]
    clasif = BlackHoleClassifier()
    List_classifier(lista,clasif).classify_list()
    

if __name__ == '__main__':
    main()