# String Variable declaration #
var_str1 = 'Hello World!'
var_str2 = "Hello World!"

print(var_str1)
print(var_str2)

#String Index
print(var_str1[0])
print(var_str1[-1])

#Index Range
print(var_str1[3:5])
print(var_str1[:5])
print(var_str1[2:-2])

# Raw String - Used for declaring regex #
var_str = r"\nHello Python World!"
print(var_str)

# String .format method #
py_version = 3
var_str = "Hello Python{} World!".format(py_version)
print(var_str)

# Multi line String #
var_str = """\
uuuuuuuuuuuuuuuuuuuuuu
iiiiiiiiiiiiiiiiiiiiii
oooooooooooooooooooooo
"""
print(var_str)