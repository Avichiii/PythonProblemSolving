def isPP(n):
    for first in range(2, n+1):
        for second in range(2, n+1):
            if first ** second > n:
                break
            elif first ** second == n:
                return [first, second]
    
    return None


print(isPP(16))