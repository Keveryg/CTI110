def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_feb(year):
    if leap_year(year):
        return 29
    else:
        return 28

def main():
    year = int(input())
    feb_days = days_in_feb(year)
    print(f"{year} has {feb_days} days in February.")

if __name__ == '__main__':
    main()
    