"""
WAP to sum all the digits of a three-digit number
input: 573
output: 15
"""

"""Write a Python program to combine two dictionaries by adding values for 
common keys.  
d1 = {'a': 100, 'b': 200, 'c':300} d2 = {'a': 300, 'b': 200, 'd':400}  
output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}  
"""
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
result = {}
for key in d1:
    result[key]=d1[key]
for key in d2:
    if key in result:
        result[key] +=d2[key]
    else:
        result[key] = d2[key]
print(result)            
    
# from collections import counter
# d1 = {'a': 100, 'b': 200, 'c':300} 
# d2 = {'a': 300, 'b': 200, 'd':400}  
# final_result = counter(d1) + counter(d2)
# print(final_result)

"""2. Write a Python program to count the number of even and odd numbers in a 
series of numbers 
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)  
Expected Output : 
Number of even numbers : 5 
Number of odd numbers : 4 
"""

