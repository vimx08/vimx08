# exe-1::
class cars:
    carname = "tesla"
    carname1 = "toyota"
    def __init__(self,color,quantity,country):
        self.color=color
        self.quantity=quantity
        self.country=country       
car1 = cars("red",3,"america")
car2 = cars("black",20,"japan")
print(car1.carname)
print(car1.color)
print(car1.quantity)
print(car1.country)

               ###################

print(car2.carname1) # toyota"
print(car2.color) # black
print(car2.quantity) # 20
print(car2.country) # japan

# exp-2::
class student:
    classroom = 12
    def __init__(self,name,age,address,height):
        self.name=name
        self.age=age
        self.address=address
        self.height=height
student1 = student("ram",22,"ktm",5.6)
print(student1.classroom)
print(student1.name)
print(student1.age)
print(student1.address)

# exp-3
class persion:
    def __init__(self,name,age,address):
        self.name="name :",name
        self.age=age
        self.address=address
p1 = ("hema",23,"bkt")
print(p1)


# exp-4
class catagory:
    subclass = ("friuts")
    def __init__(self ,apple,banana,kiwi,mango):
        self.apple=apple
        self.banana=banana
        self.kiwi=kiwi
        self.mango=mango
friuts = catagory("apple","banana","kiwi","mango")
print(friuts.subclass)
print(friuts.apple)

            #################
class catagory:
    def __init__(self ,apple,banana,kiwi,mango):
        self.apple=apple
        self.banana=banana
        self.kiwi=kiwi
        self.mango=mango
friuts = ("apple","banana","kiwi","mango")
print("this is a friuts catagory : ",friuts)