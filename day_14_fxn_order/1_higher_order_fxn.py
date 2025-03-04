# If a function takes another function as an argument then such a function is called higher order function

a = [(5, 2), (1, 1), (7, 0), (10, 12)]
def get_second(element):
    return element[1]
a.sort(key=get_second)  # Here sort() is a higher order method / function
print(a)  # [(7, 0), (1, 1), (5, 2), (10, 12)]


students = [
    {"name": "Jon", "age": 15, "address": "KTM"},
    {"name": "Jane", "age": 20, "address": "PKR"},
    {"name": "Alex", "age": 27, "address": "BKT"},
    {"name": "Hary", "age": 10, "address": "LTP"},
    {"name": "Arya", "age": 17, "address": "DHD"},
]

def get_age(element):
    return element["age"]
students.sort(key=get_age)
print(students)  # [{}, {}, {}, {}, {}]
result = sorted(students, key=get_age)
print(result)


data = [(4,5),(6,7),(8,9),(1,2),(3,11),(22,33),(100,4)]
def get_order(element):
    return element[1]
data.sort(key=get_order)
print(data)

data = [2,3,1,4,5,6,7,8,9]
def get_order(number):
    return number[1]
data.sort(key=get_order)
print(data)











