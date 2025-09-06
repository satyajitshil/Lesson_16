try:
    x = int(input("Number:"))
    print(x)
except ValueError as ex:
    print("Exception:",ex)

print("I am out of the try loop")