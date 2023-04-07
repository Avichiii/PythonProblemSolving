# def three_details(n):
#     odd_number = 0
#     even_number = 0
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             even_number += 1
#         else:
#             odd_number += 1
#     new_join_odd_number = 0

#     store_number = []
#     if even_number  % 3 == 0:
#         if even_number == 3:
#             store_number.append(even_number)
#         else:
#             new_join_odd_number = odd_number + even_number

#     if odd_number % 3 == 0:
#         if odd_number == 3:
#             store_number.append(odd_number)
#         else:
#             return three_details(odd_number)
#     elif new_join_odd_number > 0:
#         return three_details(new_join_odd_number)
    
#     if store_number != []:
#         return len(store_number)
#     else:
#         return 0

# print(three_details(15))