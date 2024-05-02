# write a program that calculates & display the letter grade given numerical score (eg_ A,B,C,D or F)
# based on following grading scale:-

# input - score - 89
# output - B
# A: 99-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

scale = int(input("Enter the number you got! "))

if scale >= 90 and scale <= 100:
    print("Your Grade is A")

elif scale >=80 and scale <= 89:
    print("Your Grade is B")

elif scale >=70 and scale <= 79:
    print("Your Grade is C")

elif scale >=60 and scale <= 69:
    print("Your Grade is D")

elif scale >=0 and scale <= 59:
    print("Your Grade is F")

else:
    print("Invalid number")


