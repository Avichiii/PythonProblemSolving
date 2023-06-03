class VendingMachine:
    def __init__(self, num_items, num_price):
        self.num_items = num_items
        self.num_price = num_price
        
    def buy(self, req_items, money):
        if self.num_items < req_items:
            raise ValueError("Not enough items in the machine")
        
        total_price = req_items * self.num_price
        if money < total_price:
                raise ValueError("Not enough coins")
           
        self.num_items -= req_items
        change = money - total_price
        return change
    