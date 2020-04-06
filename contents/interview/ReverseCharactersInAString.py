str = "Palindrome"[::-1]
print(str)

str2 = "The sky is blue"
print(str2.split(' '))

for s in reversed(str2.split(' ')):
    print(s,end=' ')

print()

for s in reversed(str2.split(' ')):
    print(s[::-1],end=' ')