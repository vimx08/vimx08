# data = "harry"
# reversed_str = data[::-1]
# if data == reversed_str:
#     print("palindrome")
# else:
#     print("not palindrome")    


# Palindrome check
# Palindrome are the words which are same even if they are reversed


# data = "madam"
# reversed_str = data[::-1]
# if data == reversed_str:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


number = 121 # interview question
n = number
rev = 0
while number != 0:
    remain = number % 10  # 1  2  1
    rev = rev * 10 + remain  # 121
    number = number // 10  # 12  1  0

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


count = 123
n = count
rev = 0
while count:
    remain = count % 10
    rev = rev * 10 + remain
    count = count // 10
if n == rev:
    print("its palindrome")
else:
    print("its not palindrome")      



# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

# def nearest_palindrome(num):
#     while not is_palindrome(num):
#         num += 1
#     return num

# number = 121
# palindrom = nearest_palindrome(number)
# print(palindrom)
e