def main():
    count = 0
    weekday = 1
    month_day = 0
    month = 0
    year = 1901
    while year < 2001:
        if weekday == 6 and month_day == 0:
            count += 1
        
        weekday = (weekday + 1) % 7
        month_day = (month_day + 1) % month_len(month, year)
        if month_day == 0:
            month = (month + 1) % 12
        if month == 0 and month_day == 0:
            year += 1
    
    print(count)

def month_len(month, year):
    if month in [0, 2, 4, 6, 7, 9, 11]:
        return 31
    elif month in [3, 5, 8, 10]:
        return 30
    else:
        if year % 400 == 0:
            return 28
        elif year % 4 == 0:
            return 29
        else:
            return 28

main()