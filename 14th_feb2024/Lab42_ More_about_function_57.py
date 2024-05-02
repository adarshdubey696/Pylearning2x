# Some more about function

# def say_hello_args(name, age): # Non return type function, which does't return any input
#     print("Hello", name, age)
#
#
# say_hello_args("My name is Adarsh, and I'M", 28)

# 2nd method "default function"
def say_hello_args_default(first_name= "Shivam", Last_name= "kumar"):
    print("Hello", first_name, Last_name)

say_hello_args_default()
say_hello_args_default(first_name="atul", Last_name= "kumar") # allowed to call and print any type of value


