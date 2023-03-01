def unique_in_order(sequence):
    sequence = list(sequence)
    stack = []
    for i in sequence:
        if stack == [] or stack[-1] != i:
            stack.append(i)
        elif stack[-1] == i:
            pass
    print(stack)


unique_in_order([1, 2, 3, 3, -1])
