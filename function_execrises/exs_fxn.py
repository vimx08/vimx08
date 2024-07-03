# 1. Write a  Python function to find the maximum of three numbers.
def maximum(value1,value2,value3):
    """find the maximum value of three numbers"""
    max_value = value1
    if value1 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value  

result = maximum(3,4,6)    
print(result) 

res = maximum('red','gren','blue')
print(res)

ult = maximum(23.05,23.005,-23.05)
print(ult)

# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# sample_list = (8, 2, 3, 0, 7)
# def sum(num):
#     total = 0
#     for i in num:
#         total += i
#     return total
# result = sum(8,2,3,0,7)
# print(result)   
      
"""3. Write a  Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336"""



"""4. Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""