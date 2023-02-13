'''
    strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

    Concatenate the consecutive strings of strarr by 2, we get:

    treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
    folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
    trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
    blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
    abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

    Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
    The first that came is "folingtrashy" so 
    longest_consec(strarr, 2) should return "folingtrashy".

    In the same way:
    longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

'''

def longest_consec(strarr, k):
    strarr = list(strarr)
    k = int(k)

    if strarr == []:
        print('')
    elif k > len(strarr):
        print('')
    elif k < 0:
        print('Positive Int plz.')
        exit()
    
    result = []
    # we are going to use window sliding
    '''
        len(strarr) = 6 - 1 = 5; 
        so total range is 5 which is what we want 0 to 5
    '''
    for i in range(len(strarr) - 1):
        
        # This will only save the slice mention in k

        '''
            in this case i = 0 and k = 2; then i will be 1 and so on...
            so [i:i+k] = 0:2; that will store 0 and 1 index
        '''
        current_window = strarr[i:i+k]
        # We are going to join that window
        current_concatenated = ''.join(current_window)
        # Append current_concatenated to result
        result.append(current_concatenated)

    # Max will only pick the max len string from the index
    long_str = max(result, key=len)
    print(long_str)

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)