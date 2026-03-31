# Encapsulation - > class ke ander ka data outsider na dkh paye 

# Attribute 
# 1. public -> a = 'smaple'
# 2. private ->  __a = sample   
# 3. proctected  -> _a = 'smaple'  


class encapsu:
    def __init__(self):
        self.name = "this is public attribute "
        self._age = "this is proctected attribute "
        self.__year = "this is private attribute "

    def show(self):
        print(f"{self.name}")
        print(f"{self._age}")
        print(f"{self.__year}")

obj = encapsu