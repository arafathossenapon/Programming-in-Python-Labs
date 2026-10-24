base = float (input("Enter the base: "))
exponent = int (input("Enter the exponent: "))


if exponent < 0:
    print("Exponent should be a non-negative integer.") 
else:
    result =1

    for i in range(exponent):
        result *= base

    print("result =", result)
    