# first
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys



# class Car:
#     def __init__(self, speed, unit):
#         self.speed = speed
#         self.unit = unit
#         if unit == "km/h":
#             return 'Car with the maximum speed of {} km/h'.format(speed)

        

# class Boat:
#     def __init__(self):
#         pass
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     q = int(input())
#     queries = []
#     for _ in range(q):
#         args = input().split()
#         vehicle_type, params = args[0], args[1:]
#         if vehicle_type == "car":
#             max_speed, speed_unit = int(params[0]), params[1]
#             vehicle = Car(max_speed, speed_unit)
#         elif vehicle_type == "boat":
#             max_speed = int(params[0])
#             vehicle = Boat(max_speed)
#         else:
#             raise ValueError("invalid vehicle type")
#         fptr.write("%s\n" % vehicle)
#     fptr.close()

#SEcond
#!/bin/python3

import math
import os
import random
import re
import sys


# class Item:
#     def __init__(self,item):
#         self.item = item
        

# class ShoppingCart:
#     # Implement the ShoppingCart here
#     pass

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())
#     items = []
#     for _ in range(n):
#         name, price = input().split()
#         item = Item(name, int(price))
#         items.append(item)

#     cart = ShoppingCart()

#     q = int(input())
#     for _ in range(q):
#         line = input().split()
#         command, params = line[0], line[1:]
#         if command == "len":
#             fptr.write(str(len(cart)) + "\n")
#         elif command == "total":
#             fptr.write(str(cart.total()) + "\n")
#         elif command == "add":
#             name = params[0]
#             item = next(item for item in items if item.name == name)
#             cart.add(item)
#         else:
#             raise ValueError("Unknown command %s" % command)
            
#     fptr.close()

