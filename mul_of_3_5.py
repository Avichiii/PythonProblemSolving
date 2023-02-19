'(solution(5), 3)'

def solution(number):
    if number == 0 or number <= 3:
        return 0
    if 3 < number:
        lst_3_5 = set()
        for i in range(1,number):
            format_3 = i*3
            if format_3 < number:
                lst_3_5.add(format_3)
        
            format_5 = i*5
            if format_5 < number:
                lst_3_5.add(format_5)

            # check's so the format's doesn't exceed the number
            if format_3 >= number and format_5 >= number:
                break

        # print(lst_3_5)
        sum_ = 0
        for l in lst_3_5:
            sum_ += l
        print(sum_)
        
solution(16)