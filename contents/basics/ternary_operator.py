division = lambda x, y : x / y
print("Case 1 : {}/{} : {}".format(4, 2, division(4, 2)))

#ternary operator with lambda
safe_division = lambda x ,y: division(x, y) if y > 0  else "ERROR :: {} cannot be divided 0".format(x)
print("Case 2 : {}/{} : {}".format(4, 0, safe_division(4, 0)))