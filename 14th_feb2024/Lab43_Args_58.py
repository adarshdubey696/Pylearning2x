# #1st method
# def print_argument(*args): # It is consider as a list type function
#     for i in args:         # in this case use "i" to list all the function
#         print(i,end=" ")
#
# print_argument(1)
# print_argument(1, 2, 3)
# print_argument(4, 5, 6, 7, 8)

# 2nd method
def print_pizza(*toppings):
    for t in toppings:
        print(t, end= " ")


sonam = print_pizza("onion", "paneer", "red chilli")

