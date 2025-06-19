# Lambda Expression with single input

double = lambda x: 2*x

print(double(4))

list_of_authors =['Krishna Menon','Ruskin Bond','Chethan Bagat','Jeevan Arya']
list_of_authors.sort(key=lambda name: name.split(" ")[-1])
print(list_of_authors)


#Function returning functions
def build_quadratic_function(a,b,c):
    return lambda x: a*x**2+b*x+c

q = build_quadratic_function(3,2,1)

print(q(2))
print(build_quadratic_function(3,2,1)(2))