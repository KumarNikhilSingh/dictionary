def greet(name):
    return f"Hello, {name}"  
greet_variable = greet
print(greet_variable("Rupali"))

#define function 'greet' that takes name as an argument
#assign the function 'greet' to the variable 'greeet_variable'
#call the function using 'greet_variable'

'''

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def apply_operation(operation, a, b):
    return operation(a, b)
addition = add
subtraction = subtract
print(apply_operation(addition, 5, 3))   
print(apply_operation(subtraction, 5, 3))
'''
#'apply_operation'takes another function takes another function ('operation')
#a, b as arguments then call the operation by assigning the 'add' and 'subtract