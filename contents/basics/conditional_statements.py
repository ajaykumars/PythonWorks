a = 2;
b = 1;
if a > b:
    print("a with value ({}) is greater than b with value ({})".format(a, b))
elif a < b :
    print("a with value ({}) is lesser than b with value ({})".format(a, b))
else :
    print ("a is equal to b")

print ("foo" if a < b else "bar")

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

