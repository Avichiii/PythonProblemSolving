#solve([2,3,5,3,7,9,5,3,7]),[3,3,3,5,5,7,7,2,9])

def solve(arr):
    # -arr.count() represent decending order
    # (-arr.count(x),x) is a tuple
    arr = sorted(arr, key = lambda x: (-arr.count(x),x)) 
    print(arr)

solve([2,3,5,3,7,9,5,3,7])