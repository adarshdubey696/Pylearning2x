# Leap Year Checker

Leap_Year = int(input("Enter the number! "))

if 2024%4:
    print("The year is leap year")

elif 2024%100:
    print("The year is not leap year")

elif 2024%400:
    print("The year is leap year")

else:
    print("Invalid number")