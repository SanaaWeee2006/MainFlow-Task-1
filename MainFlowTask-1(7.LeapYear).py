# 7. Determine whether a year is a leap year.

#divivsible by 4 and  not divisible by 100 , divisible by 400

year = int(input("Enter the year to check: "))

def is_leap_year(year):
    return (year %4 ==0 and year %100 != 0) or (year %400 == 0)

leap_year = is_leap_year(year)
print(f'{year} is a leap year ? : ', leap_year)
