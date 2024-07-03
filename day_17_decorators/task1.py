# Create a decorator function which when applied to another function (that returns a string), it gives
# the uppercase value

# def to_upper(fxn):
#     def inner_func(*args):
#         msg = fxn(*args)
#         return msg.upper()
#         return fxn(*args).upper()

# @to_upper
# def display(msg):
#     return msg
# result = display("hello world")
# print(result)



def upper_func(func):
    def inner_fxn(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return inner_fxn

@to_upper
def display(msg):
    return msg
result = display("hello world")
print(result)