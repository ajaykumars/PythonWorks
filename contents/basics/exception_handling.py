try:
    int(2.0)
    int('string')
    int([1,2,3])
    print("Success")
except (ValueError, TypeError):
    print("Failure")

try:
    a = 1/0
except ZeroDivisionError:
    print("Operation Not Allowed")

