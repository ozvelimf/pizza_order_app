from files.model.app_model import *
# ==================== Pizza üst sınıfı =================== #
class Pizza():
    def __init__(self, pizza_input):
        self.pizza_order = dict()
        self.__cost, self.__description = get_pizza_info(pizza_input, self.pizza_order)
        
    def get_cost(self):
        return self.__cost
    
    def get_description(self):
        return self.__description       


# ============= Pizza sınıfının alt sınıfları ============= #

# Klasik pizza
class Classic(Pizza):
    def __init__(self, pizza_input):
        super().__init__(pizza_input)

# Margarita pizza
class Margarita(Pizza):
    def __init__(self, pizza_input):
        super().__init__(pizza_input)

# Türk pizza
class Turkish(Pizza):
    def __init__(self, pizza_input):
        super().__init__(pizza_input)

# Sade pizza
class Plain(Pizza):
    def __init__(self, pizza_input):
        super().__init__(pizza_input)









    

