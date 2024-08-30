'''
In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

["January","February","March","April","May","June","July","August","September","October","November","December"]

Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
'''

def main():
    # Get the date from the user
    date_input = input("Enter a date (MM/DD/YYYY or Month Day, Year): ")
    convert_date(date_input)

def convert_date(input_date):
    # List of month names
    months = ["January", "February", "March", "April", "May", "June", "July","August", "September", "October", "November","December"]

    while True:
        try:
            # Check if the date is in MM/DD/YYYY format
            if '/' in input_date:
                month, day, year = input_date.split('/')
                month, day, year = int(month), int(day), int(year)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break

            # Check if the date is in Month Day, Year format
            else:
                month_day, year = input_date.split(',')
                month_name, day = month_day.split()
                day, year = int(day), int(year.strip())

                if month_name in months and 1 <= day <= 31:
                    month = months.index(month_name) + 1
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break

        except (ValueError, IndexError):
            pass

        # If the input is invalid, prompt again
        input_date = input("Invalid date format. Please enter the date again: ")

main()
