'''
In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
'''

def main():
    groceries = {}

    # prompt user for items, one per line, until user inputs control-d
    while True:
        try:
            prompt = input().strip().upper()
            if prompt not in groceries:
                groceries[prompt] = 1
            else:
                groceries[prompt] += 1

        except EOFError:
            # output groceries alphabetically, prefixed with number of times inputted
            for item in sorted(groceries):
                print(f"{groceries[item]} {item}")
            break

if __name__ == "__main__":
    main()
