string_list = ["flowes","flower", "flowe"]
index = 0
common_sub_string = ''

min_str_length = min([len(word) for word in string_list])
match_complete = False

for itr in range(min_str_length):
    for word in string_list:
        char_to_match = word[index]
        if word[index] != char_to_match:
            match_complete = True
            break;
    if(match_complete):
        break
    common_sub_string = common_sub_string + string_list[0][itr]

print(common_sub_string)

