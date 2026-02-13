import math

# RELATIVE IMPORTS - importing from same package and other packages
from .basic import add,multiply,divide,subtract # Same package (math_ops)
from ..utils.helper import validate_number,format_result #Different package (utils)


def square_root(number):
    """ Square root with validation using relative imports"""
    #Use relative import from utils
    if not validate_number(number):
        return "Error : Invalid number"
    
    if number<0:
        return "Error : cannot calculate square root of negative number"
    
    result = math.sqrt(number)
    #Use relative import from utils to format
    return format_result(result)

def power(base,exponent):
    """" Power calculation using relative imports """
    # Use relative import from same package
    if exponent==0:
        return 1
    elif exponent==1:
        return base
    elif exponent ==2:
        return multiply(base,base) #Using relative import
    else:
        result = base ** exponent
        return format_result(result)
    

def factorial(n):
    """ Factorial using relative imports """
    if not validate_number(n) or n<0:
        return "Error : Invalid input for factorial"
    
    if n <=1:
        return 1
    
    #Calculate factorial using relative import (add)
    result = 1
    for i in range(2,int(n)+1):
        result = multiply(result,1) #Using relative import

    return format_result(result)


def compound_calculation(num1,num2,num3):
    """Demonstrate multiple relative imports"""
    #Use multiple relative imports from same package
    step1 = add(num1,num2)
    step2 = multiply(step1,num3)

    #Use relative import from different package
    return format_result(step2)
