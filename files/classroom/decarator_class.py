from files.classroom.pizza_class import Pizza
from files.classroom.souce_class import Souce

class Decorator():
    def __init__(self, pizza:Pizza, souce:Souce):
        self.__pizza = pizza
        self.__souce = souce
    
    def get_cost(self):
        return self.__souce.get_cost() + self.__pizza.get_cost()
    
    def get_description(self):
        return self.__souce.get_description() + ' ' + self.__pizza.get_description()
