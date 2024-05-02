# Continue function

#1st method, Print the value in increase order
# for num in range (1,10):
#     if num > 2:  # Is case me mentioned condition se "badaa number" print hoga.
#         print(num)

# 2nd method, Print even & odd number by using Contine function
# for num in range (1,10):
#     if num % 2 == 0:  # In this case value will printed till it mentioned range "f" is used for formatting purpose
#         print(f"Even number {num}")
#     else:
#         print(f"Odd number {num}")


# 3rd method, Another method of writing even and odd number
for num in range (1,10):
    if num % 2 == 0:
        print(f"Even number {num}")
        continue # If code is written till here then only "even num" will be printed
    print(f"Mentioned odd number {num}") # Jab ye line likhenge tab hi "odd num" print hoga