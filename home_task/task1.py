"""Write a Python program to combine two dictionaries by adding values for 
common keys.  
d1 = {'a': 100, 'b': 200, 'c':300} d2 = {'a': 300, 'b': 200, 'd':400}  
output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}  """
def combine_dictionaries(d1, d2):
    combined_dict = d1.copy()  # Start with a copy of the first dictionary
    
    for key, value in d2.items():
        if key in combined_dict:
            combined_dict[key] += value  # Add values for common keys
        else:
            combined_dict[key] = value  # Add new key-value pairs
    
    return combined_dict
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
result = combine_dictionaries(d1, d2)
print(result) 


"""Write a Python program to count the number of even and odd numbers in a 
series of numbers 
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)  
Expected Output : 
Number of even numbers : 5 
Number of odd numbers : 4 
"""
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count, odd_count = count_even_odd(numbers)
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
