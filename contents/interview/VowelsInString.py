input = 'abacda'
# vowels_list = ['a','e','i','o','u']
vowels_count = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
for ch in input:
    if(ch in vowels_count.keys()):
        vowels_count[ch]+= 1

print(vowels_count)

