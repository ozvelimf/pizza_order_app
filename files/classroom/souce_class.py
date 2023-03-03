from files.model.app_model import *
# ==================== Source üst sınıfı =================== #
class Souce():
    def __init__(self, souce_input):
        self.souce_order = dict()
        self.__cost, self.__description = get_souce_info(souce_input, self.souce_order)

    def get_cost(self):
        return self.__cost
    
    def get_description(self):
        return self.__description    


# ============= Source sınıfının alt sınıfları ============= #

# Zeytin sosu
class Olive(Souce): 
    def __init__(self, souce_input):
        super().__init__(souce_input)

# Mantar sosu
class Mushroom(Souce):
    def __init__(self, souce_input):
        super().__init__(souce_input)

# Keçi peyniri sosu
class GoatCheese(Souce):
    def __init__(self, souce_input):
        super().__init__(souce_input)

# Et sosu
class Meat(Souce):
    def __init__(self, souce_input):
        super().__init__(souce_input)

# Soğan sosu
class Onion(Souce):
    def __init__(self, souce_input):
        super().__init__(souce_input)

# Mısır sosu
class Sweetcorn(Souce):
    def __init__(self, souce_input):
        super().__init__(souce_input)