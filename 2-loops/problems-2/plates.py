"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”

“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

“No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""

def main():
    # take input 
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

    def is_valid(s):
        txt=""
        num=""
        # check length is >= 2 and >= 6 and contains no invalid chars
        if len(s) >= 2 and len(s) <= 6 and s.isalnum():
            print("s is", s)
            # split string into left/right by finding the first numeric char and making that the first char in the right part
            for i in s:
                if(i.isdigit()): num+=i
                else: txt+=i
        else: 
            print("Ooops")
            
        # check that the left part is at least 2 in length
        print(txt)
        # check that the right part doesn't start with 0
        # check that the right part is all numbers (.isnumeric())
        print(num)

main()


