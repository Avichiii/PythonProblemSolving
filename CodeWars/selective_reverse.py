'([2,4,6,8,10,12,14,16], 3), [6,4,2, 12,10,8, 16,14])'

def sel_reverse(arr,l):
    arr = list(arr)
    result = []
    if l == 0:
        print(arr)
    # start, stop, step: start from 0 stop at 7 and hop 3 steps
    for i in range(0, len(arr), l):
        current_window = arr[i:i+l]
        for j in current_window[::-1]:
            result.append(j)
    print(result)

sel_reverse([2,4,6,8,10,12,14,16], 3)