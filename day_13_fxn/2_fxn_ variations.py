# Python function variations are as follow

# 1. With Parameter and With Return
# Here a and b are parameters and their sum is return
def addition(a, b):
    """

    :param a: integer type
    :param b: integer type
    :return: Sum of a and b. Integer type
    """
    return a + b

# function call
result = addition(2, 3)
print(result)

result = sum((1, 2, 3))
print(result)

result = sum([1, 2, 3], 7)
print(result)


# Without parameter with return
def message():
    return "Hello World"
result = message()
print(result)  # Hello World

def number():
    return("this have no number")
result = number()
print(result)

# With parameter without return
def addition(a, b):
    if type(a) != str or type(b) != str:
        return "Invalid type of a or b"
    c = a + b
    print(c)

result = addition(5, 4)
print(result)  # None

def multiple(a,b):
    if type(a)!=str or (b)!=str:
        return"invalid type a or b"
    c = a*b
    print(c)
result = multiple(3,4)
print(result)




# Without parameter without return
def message():
    print("Hello World")

result = message()
print(result)  # None

def number():
    print("this have no number")
result = number()
print(result)