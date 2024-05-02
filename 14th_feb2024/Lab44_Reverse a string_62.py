# Reverse a String

# 1st method, simple programme for a reverse string
# str = "Adarsh"
# rev_str = ""
# for c in str:
#     rev_str = c + rev_str
#
# print(rev_str)


# 2nd method, reverse the string by using function

def reverse_string(str):
    rev_str= ""
    for c in str:
        rev_str = c + rev_str
    return rev_str

name = reverse_string("vikram")
print(name)