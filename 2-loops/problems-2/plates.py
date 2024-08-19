'''
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
'''

def main():
# takes input and passes to is_valid to check
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check the length of the plate
    if len(s) < 2 or len(s) > 6:
        return False
    # Check if the plate starts with at least two letters
    if not s[0:2].isalpha():
        return False
    # Ensure all characters are alphanumeric
    if not s.isalnum():
        return False

    # Separate the string into letters and numbers
    letters = ""
    num = ""
    num_found = False

    for char in s:
        if char.isdigit():
        # Entering numeric phase. If digit has been encountered, no letters are allowed to follow
            num_found = True
            num += char
        elif not char.isdigit() and num_found == True:
            # If a letter appears after a number has started, it's invalid
            return False
        else:
            letters += char

    # Check if numbers are present and if the first number is not '0'
    if len(num) > 0 and num[0] == '0':
        return False

    return True

main()