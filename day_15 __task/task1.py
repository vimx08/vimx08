#Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def get_unique(list):
    result = []
    for each in list:
        if each not in result:
            result.append(each)
    return result 
data = [1,2,3,3,3,3,4,5]  
res = get_unique(data)
print(res)

# comprehension::
data = [1,2,3,3,3,3,4,5]
def get_unique(list):
    result = []
   [result.append(each) for each in list if each not in list]
    return result
data = [1,2,3,3,3,3,4,5]  
res = get_unique(data)
print(res)

# # by using lambda:
# data = [1,2,3,3,3,3,4,5]
# def new_function(element):
# data.sort(key= lambda elemen : elemen[1])
