try:
    num1 = int(input("Number:"))
    num2 = int(input("Number:"))
    value = num2/num1
    print("the answer is",value)
    print("the answer is", value1)
except ZeroDivisionError as ex:
    print("The Division by Zero is not allowed. the exception is",ex)
except ValueError as ex:
    print("Value is not correct. Enter a numeric value")
except NameError as ex:
    print("The exception is",ex)
except:
    print("Error occured")
finally:
    print("Inspite of all errors I will execute.")