def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        if isinstance(a,(int, float)) and isinstance(b,(int, float)):
            return "Invalid input types"
        else:
            return "One or both inputs are not numbers"

#this is the way to reproduce it 
result1 = function_with_uncommon_error(10, 0)  #Produces "Division by zero"
result2 = function_with_uncommon_error(10, 2)  #Produces 5.0
result3 = function_with_uncommon_error(10, "hello") #Produces "One or both inputs are not numbers"
result4 = function_with_uncommon_error("hello", 2) #Produces "One or both inputs are not numbers"
print(result1, result2, result3, result4)