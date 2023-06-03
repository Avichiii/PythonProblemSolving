class Car:
    def __init__(self, maximum_speed, mph):
        self.maximum_speed = maximum_speed
        self.mph = mph
        
    def __str__(self):
        print(f'Car with the maximum speed of {self.maximum_speed} {self.mph}')
        

class Boat:
    def __init__(self, speed)->str:
        self.speed = speed
        
    def __str__(self):
        return f'Boat with the maximum speed of {self.speed} knots'
    
car = Car(151, 'km/h')
boat = Boat(77)

print(car)
print(boat)