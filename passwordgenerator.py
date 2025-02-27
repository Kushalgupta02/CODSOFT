import random
import string

def generatepass(length, useuppercase=True, usedigits=True, usespecial=True):
    characters = string.ascii_lowercase
    if useuppercase:
        characters += string.ascii_uppercase
    if usedigits:
        characters += string.digits
    if usespecial:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    useuppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    usedigits = input("Include digits? (y/n): ").lower() == 'y'
    usespecial = input("Include special characters? (y/n): ").lower() == 'y'

    password = generatepass(length, useuppercase, usedigits, usespecial)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()