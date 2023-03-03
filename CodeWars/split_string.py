def solution(s):
    s = str(s)
    if s == '':
        return []
    elif len(s) == 1:
        return [s + '_']
    
    pair_s = []
    # the loop is skipping two elements
    for i in range(0,len(s), 2):
        # the window is of two elements
        current_window = s[i:i+2]
        if len(current_window) != 1:
            pair_s.append(current_window)
        else:
            mod = current_window + '_'
            pair_s.append(mod)

    return pair_s
print(solution('asdfadsf'))