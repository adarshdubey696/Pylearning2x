# Filter
# > It basically filter the item from the list based on the logic
# > it will return less number of items

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = filter(lambda item: item % 2 == 0, numbers)
# print(list(even_numbers))  # Convert the filter object to a list and print it


# 2nd method, Filter by function
def even(num):
    return num % 2 == 0


numbers = [36, 34, 36, 41, 45]
even_numbers = filter(even, numbers)
print(list(even_numbers))
