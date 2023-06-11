'''
class 

    1. insert ( no duplicates )
    2. remove
    3. getRandom value that is already in the class
'''
import random

class Store:
    def __init__(self):
        self.list = []

    def insert(self, value:int):
        if len(self.list) == 0:
           self.list.append(value)
        else:
            if value not in self.list:
                self.list.append(value)

    def remove(self, value:int):
        if self.list == []:
            return
        else:
            if value in self.list:
                self.list.remove(value)
            else:
                raise ValueError('Value isn\'t present')

    def getRandom(self):
        try:
            return random.choice(self.list)
        except:
            raise ValueError('Value isn\'t present')

    def view(self):
        try:
            entireList = ''
            for value in self.list:
                entireList += f'{value} -> '

            return entireList    
        except:
            raise ValueError('Value isn\'t present')
        
store = Store()


