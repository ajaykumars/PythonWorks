mylist = [1, 2, 4, 2, 5]

string_list = ["abc", "elephant", "i", "strong"]

print(max(set(mylist), key=mylist.count))
print(max(string_list, key=len))

# print(mylist.count())