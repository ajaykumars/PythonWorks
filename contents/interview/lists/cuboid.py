# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())

x = 2
y = 2
z = 2
n = 4
# list = [sum([a for a in range(x+1)]) if != n  for b in range (3)]

print([ [ i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range( z + 1) if ( ( i + j + k ) != n )])

# print(list)
