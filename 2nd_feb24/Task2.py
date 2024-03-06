#Task #2 - Print the Table of 2 by using the command print()
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 10 = 20
# Use printf command

# Method 1st
# for i in range(1, 11):
#     print(f"2 x {i} = {2*i}")

# Method 2nd
# for i in range(1, 11):
#     print("2 *", i, "=", 2 * i)

# Method 3rd
# format string
num = 2
print(f"{num}*1 = {num}")
print(f"{num}*2 = {num*2}")
print(f"{num}*3 = {num*3}")
print(f"{num}*10 = {num*10}")