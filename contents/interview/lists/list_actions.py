n = int(input())
list = []
for i in range(n):
    action = str(input()).split()
    if (action[0] == "insert"):
        list.insert(int(action[1]), int(action[2]))
    elif (action[0] == "print"):
        print(list)
    elif (action[0] == "remove"):
        list.remove(int(action[1]))
    elif (action[0] == "append"):
        list.append(int(action[1]))
    elif (action[0] == "sort"):
        list.sort()
    elif (action[0] == "pop"):
        list.pop()
    elif (action[0] == "reverse"):
        list.reverse()
print(list)
