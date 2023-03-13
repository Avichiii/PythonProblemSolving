'''
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
'''
from string import ascii_uppercase
def to_underscore(string):
    snake_case = ''
    for index, i in enumerate(str(string)):
        print(index, i)
        if i in ascii_uppercase:
            if index == 0:
                snake_case += i.lower()
            else:
                snake_case += '_' + i.lower()
        else:
            snake_case += i 
    return snake_case
            

print(to_underscore('App7Test'))
