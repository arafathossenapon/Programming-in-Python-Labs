char = input("Enter a character: ")


if len(char) != 1:
    print("Please enter a single character.")
elif char.lower() in 'aeiou':
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowel.")