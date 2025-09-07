try:
    x = int(input("Number:"))
    print(x)
except ValueError as ex:
    print("Exception:",ex)

print("You are out of the try loop")