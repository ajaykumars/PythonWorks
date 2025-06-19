import pytest

assert True

x=-1
if(x > 0):
    print("greater")
elif(x == 0):
    print("equal")
else:
    print("lesser")



for i in range(5,10):
    print(i)

i=10
while(i>0):
    print(i)
    i = i-1


dlist = ['abc','def']
dtuple = ('abc','def')
ddict = {0:'abc',1:'def'}

print(ddict)

multipler = lambda x: lambda y:x*y

print(multipler(2)(8))


str = "abcdef"
print(str[::-1])

print(type(str))


even_numbers = [num for num in range(2,11,2)]
print(even_numbers)
print(type(even_numbers))


even_numbers_set = (num for num in range(2,11,2))
print(even_numbers_set)
print(type(even_numbers_set))

for n in even_numbers_set:
    print(n)


try :
    x = 1/0
except ZeroDivisionError :
    print('ZeroDivisionError occured')
finally:
    print('roll back operation')


func = lambda x : x*2;

print(func(2))

int_list = [num for num in range(1,11,2)]

for index, num in enumerate(int_list):
    print("index : {} with value : {}".format(index, num))

print([num for num in reversed(int_list)])
print(max(int_list))
