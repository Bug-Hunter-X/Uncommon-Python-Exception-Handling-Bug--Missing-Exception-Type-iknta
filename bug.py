def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input types"

#this is the way to reproduce it 
result1 = function_with_uncommon_error(10, 0)  #Produces "Division by zero"
result2 = function_with_uncommon_error(10, 2)  #Produces 5.0
result3 = function_with_uncommon_error(10, "hello") #Produces "Invalid input types"
print(result1, result2, result3)