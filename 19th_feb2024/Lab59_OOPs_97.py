# Programme of Calculator
#1st method

# class cal:
#     def sum(self, a, b):
#         return a+b
#
# a = cal()
# result = a.sum(3, 4)
# print(result)

#2nd method

class Cal:
    def add(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

    def multi(self, a, b):
        return a*b

    def div(self, a, b):
        return a/b

object_ref = Cal()

# final_result = object_ref.sum(5,4)
# print(final_result)

final_result = object_ref.add(5, 4)
print(final_result)  # Output: 9

final_result = object_ref.sub(5, 4)
print(final_result)  # Output: 1

final_result = object_ref.multi(5, 4)
print(final_result)  # Output: 20

final_result = object_ref.div(5, 4)
print(final_result)  # Output: 1.25

