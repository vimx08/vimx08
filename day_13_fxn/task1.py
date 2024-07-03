# Create a student dictionary.
# Create a function which takes dictionary key (string) as argument and return the value of that key


student = {"name": "Alex", "age": 30, "address": "KTM"}


def get_value(key):
    print(student,'<------>')
    r = student.get(key, "The info is not available")
    return r

student = {"name": "Alex", "age": 30, "address": "KTM","roll":"21"}
key = input("Enter the key you want to access ")
result = get_value(key)
print(result)
