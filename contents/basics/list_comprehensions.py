
str =  "lazy fox had a good morning breakfast"
str_word_len = [len(word) for word in str.split()]
print (str_word_len)

str_word_len_prime = [len(word) for word in str.split() if len(word)%2 != 0]
print (str_word_len_prime)

str_len_pairs = [(word, len(word), 'true' if len(word)%2 != 0 else 'false')for word in str.split() ]
print (str_len_pairs)
print(type(str_len_pairs.pop(3)))
print (str_len_pairs)

str_len_odd_even = [(word, len(word))for word in str.split()]


