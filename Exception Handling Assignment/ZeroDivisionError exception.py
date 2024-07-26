def divide(a,b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(e)
    
    return result
print(divide(46,2))
print(divide(10,0))    