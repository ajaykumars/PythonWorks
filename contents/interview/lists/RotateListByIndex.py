def rotate_list_by_index(list, index):
    temp_list = []
    for i in range(index + 1, len(list)):
        temp_list.append(list[i])

    for i in range(0, index+1):
        temp_list.append(list[i])

    return temp_list


list = [1,2,3,4,5,6,7,8,9,10]
index = 6
print(type(list))

print(rotate_list_by_index(list, index))



