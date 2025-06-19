from math import sqrt
import math
print(int(sqrt(9)))

print(dir(math))

# def print_list(l):
#     print(l.)

def func(t):
    if isinstance(t, str):
        print('Printing String : ')
        print(t)
    if isinstance(t, tuple):
        print('Printing Tuple : ')
        print(t)

func('one')
func(('two','three'))