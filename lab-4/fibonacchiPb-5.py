n = int(input("Enter a number: "))

a=0
b=1
while a <= n:
    print(a)
    a, b = b, a + b

print()