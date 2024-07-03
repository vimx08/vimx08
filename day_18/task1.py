# number = int(input("enter the number : "))
# counter = (0)
# if number % 2 ==0:
#     counter += 1
#     print("composite number")
#     if number % 1 == 1.5:
#         print("not a prime number")
#         if number <=1:
#             print(False)
# else:
#     print("prime")    
        
def check_prime(num):
    counter = 0
    if num <= 1:
        return("neither prime nor composite")
    else:
        for i in range(1, num+1):
            if num % i ==0:
                counter += 1
        if counter == 2:
            return("prime")
        return("composite")    
result = check_prime(12)
print(result)    

#Check whether an input number prime or composite  ## interviews qestion.
# Positive integer which have only two factors, 1 and the number itsel

def check_prime(num):
    count = 0
    if num <= 1:
        return "Neither prime nor composite"
    else:
        for i in range(1, num//2 + 1):  # 1, 2, 3, 4, 5, 6, 7, 8
            if num % i == 0:
                count += 1   # > 2
        if count >= 2:
            return "Composite"
        return "Prime"


result = check_prime(13)
print(result)

result = check_prime(7)
print(result)

result = check_prime(2)
print(result)

result = check_prime(4)
print(result)

result = check_prime(10)
print(result)
        