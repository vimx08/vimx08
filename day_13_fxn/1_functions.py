# function in python::::(vip)
# 1. Functions are the block of reusable code.
# 2. We use "def" key to create a function in python
# 3. Function names follow identifier rules. By pep-8 convention python functions should follow snake case pattern


def Addition():
    pass

def num_addition():
    pass

def NumAddition():
    pass

def num2():
    pass

# These all are valid function names

# There are two parts of a function; i) function definition ii) function call

# i= function definition
def addition(a, b):
    return a + b

# ii= function call
result = addition(2, 3)
print(result)

result = sum([1, 2, 3])
print(result)

def average(a,b):
    return (a + b)/2
result = average(6,8)
print(result)

def addition(a,b):
    return a + b
result = addition(5,15)   
print(result)

def addition(a,b):
    return (a + b) /2
result = addition(5,15)
print(result)

# data = [1,2,3,4,5,6]
# def highest_value():
#     result(highest_value,"data")
# result = highest_value(data)
# print(result)
#  what is local variable and Docsrting
# function with muitile paramerter.


result = sum([1,2,3,4])
print(result)

result = sum([1,2,3],8)
print(result)


def avg_number(a,b):
    return(a+b)/2
result = avg_number(12,32.5)
print(result)