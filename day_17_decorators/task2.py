# Create a decorator function login_required which when applied to a function, asks for password.
# If the provided password is "1234" then excute the function else return "Invalid Password. User not authenticated"

def login_required(fxn):
    def inner_func(*args,**kwargs):
        password = input("Enter password: ")
        if password == "123":
            return fxn(*args, **kwargs)
        else:
            return "invalid password User not authenticated"
    return inner_func        

@login_required
def addition(a, b, c):
    return a + b + c


result = addition(1, 2, 3)
print(result)

@login_required
def isplay(msg):
     return msg


@login_required
def display(msg):
    return msg
result = display("Hello World")
print(result) 