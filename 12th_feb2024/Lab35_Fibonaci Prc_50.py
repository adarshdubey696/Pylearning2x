# Fibonacci series:- adding the last value, to get current value.
# 0,1,1,2,3,5,8,13,21 etc

# 1st method
# a = 10
# b = 20
# a,b = a, a+b
# print(a,b)

# 2nd, method
a, b = 0, 1
while a < 10:
    print(a, end=" ") # if end=" " is not mentiond, ouptup new line me aaye ga.
    a, b = b, a+b

