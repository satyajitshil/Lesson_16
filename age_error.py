try:
    age = int(input("Enter age: "))
    print(age)
except ValueError:
    print("Invalid age")
finally:
    print("Error 404. Please Fix")