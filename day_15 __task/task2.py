# 15. Write a Python program to add two given lists using map and lambda.
# Original list:
# [1, 2, 3]
# [4, 5, 6]
# Result: after adding two list

data = [1, 2, 3]
data1 = [4, 5, 6]

# def addition(data,data1):
#     return data + data1
# result = addition(data)
# print(result)

def add_two_data(data,data1):
    result = []
    for index, value in enumerate(data):
        res= value + data1[1]
        result.append(res)
    print(result)
r = add_two_data(data,data1)
print(r)


# l1 = [1,2,3]
# l2 = [4,5,6]
# data = zip(l1,l2)

# print(list(data))
# def add_two_list(l1,l2):
#     iterable = zip(l1,l2)
#     result = map(lambda x: sum(x), zip(l1,l2))
#     return(list(data))
# res =  add_two_list(l1,l2)
# print(res)
