def square(num):
    return num*num

num_list = [i for i in range(10)]

list_of_squares = list(map(square, num_list))

print(list_of_squares)
