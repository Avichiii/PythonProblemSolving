#Q. returns "(123) 456-7890"
'''
def create_phone_number(n):
    #this takes a list of numbers and returns a ph number
    n = list(map(str, n)) # this will give a map object so we need to convert it to a list again
    
    n = list(n) #it will look like ['1','2']
    ''.join(n) # 12
    n = f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
    return n
'''

def create_phone_number(n):
    '''
        No need to typecast n to str
        the input is already taking the str
        we are doing it for fun
    '''
    n = str(n)
    if len(n) == 10:
        n = f"({n[0] + n[1] + n[2]}) {n[3]+ n[4]+ n[5]}-{n[6]+ n[7]+ n[8]+ n[9]}"
        return n
    elif len(n) == 13:
        if n.startswith('+'):
            n = f"{n[0] + n[1] + n[2]} ({n[3] + n[4] + n[5]}) {n[6]+ n[7]+ n[8]}-{n[9]+ n[10]+ n[11]+ n[12]}"
            return n
    elif len(n) < 10 or len(n) > 13:
        print("Enter 10 or 13 numbers Only")
    else:
        print("Invalid")

if __name__ == "__main__":
    num = input('Enter number <: ')
    print(create_phone_number(num))

