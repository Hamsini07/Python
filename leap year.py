def is_leap(year):
    if year % 4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")

year = int(input("Enter a year: "))
is_leap(year)
