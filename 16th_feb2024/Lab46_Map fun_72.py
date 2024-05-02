# Map () -> in-built function
# 1.Takes each item from the list
# 2.Execute the function on it.
# 3.Returns the same number of elements (list)

def sq_of_number(num):
    return num ** 2


numbers = [1, 2, 3, 4, 5]  # taking a list element

# Syntax: var = list(map(fun_name, name of list var))

sq_num = list(map(sq_of_number, numbers))
print(sq_num)

