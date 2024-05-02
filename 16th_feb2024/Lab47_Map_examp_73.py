numbers = [3, 4, 5, 6, 7]


def cube_rt(num):
    return num ** 3


cube_num = list(map(cube_rt, numbers))
print(cube_num)


# 2nd method

def cube_rt(num):
    return num ** 3


my_list = [4, 5, 6, 7]
cube_num = list(map(cube_rt, my_list))
print(cube_num)
