
'''
25-09-2005
21-08-2003

1900, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 
1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 
1996, 2000, 2004, 2008, 2012, 2016, 2020

if any of the year include any of these years, then +1 for each year.

dict = jan:31, feb:28, mar:31, apr:30, may:31, jun:30, jul:31, aug:31, sep:30, oct:31, nov:30, dec:31

month = 12

'''

def year_diff(Y1, Y2):
    # Checks if the First Year is less then Second Year
    if Y1[2] > Y2[2]:
        print('First Year needs to be less then Second Year')
        exit(0)

    # Checking Validity of Year
    if Y1[2] >= 2024 or Y2[2] >= 2024 or Y1[2] <= 1899 or Y2[2] <= 1899:
        print('Invalid Year')
        exit(0)

    # Checking Validity of Month
    if Y1[1] > 12 or Y1[1] < 1 or Y2[1] > 12 or Y2[1] < 1:
        print('Invalid Month')
        exit(0)

    # Checking Validity of Date of the Month
    if Y1[1] > 31 or Y1[1] < 1 or Y2[1] > 31 or Y2[1] < 1:
        print('Invalid Date of the Month')
        exit(0)

    # Checking Leap Years + counting Years
    count = 0
    Year_count = 0
    for year in range(Y1[2], Y2[2]):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            count +=1
        Year_count += 1

    # Months
    Month_diff = [Y1[1], Y2[1]]

    Number_of_months = []
    for i in range(min(Month_diff), max(Month_diff)+1):

          Number_of_months.append(i)


    Calander = [[1, 'jan', 31], [2, 'feb', 28], [3, 'mar', 31], [4, 'apr', 30], [5, 'may', 31], [6, 'jun', 30], [7, 'jul', 31], [8, 'aug', 31], [9, 'sep', 30], [10, 'oct', 31], [11, 'nov', 30], [12, 'dec', 31]]
    List_of_Month_days = []
    for i in Number_of_months[:-1]:
        for j in Calander:
            if i == j[0]:
                List_of_Month_days.append(j[2])

    # Day of Month
    Day_diff = [Y1[0], Y2[0]]
    Days = max(Day_diff) - min(Day_diff)

    # Converting into Days
    Total_days = Year_count * 365.2425 
    for i in List_of_Month_days:
        Total_days += i
    if count > 0:
        Total_days += count
        return Total_days + Days
    else:
        return Total_days + Days


# year_1 = list(map(int, input('Enter the First Year <: ').split()))
# year_2 = list(map(int, input('Enter the Difference Year <: ').split()))

print(year_diff([28, 10, 1991], [16, 11, 2020]))




'''
Expereimental Code

# Creating Month List
Month_list = []
for month in range(1, 12+1):
    if month == 2:
        Month_list.append(28)
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        Month_list.append(31)
    else:
        Month_list.append(30)


Mon = [[1, 'jan', 31], [2, 'feb', 28], [3, 'mar', 31], [4, 'apr', 30], [5, 'may', 31], [6, 'jun', 30], [7, 'jul', 31], [8, 'aug', 31], [9, 'sep', 30], [10, 'oct', 31], [11, 'nov', 30], [12, 'dec', 31]]

# Total = f'{Year_count} Year, {count} Leap Year, {Mon} Month, {Da} Day'

# print(C_months[0:2])

#  print(Month_diff.count(i))
'''