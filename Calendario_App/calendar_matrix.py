import calendar

def create_calendar_matrix(year, month):
    # Create a calendar object
    cal = calendar.monthcalendar(year, month)
    
    # Get the month name
    month_name = calendar.month_name[month]
    
    # Print the calendar header
    print(f"{month_name} {year}".center(20))
    print("Mo Tu We Th Fr Sa Su")
    
    # Print the calendar matrix
    for week in cal:
        for day in week:
            if day == 0:
                print("  ", end=" ")
            else:
                print(f"{day:2d}", end=" ")
        print()

# Example usage
year = 1997
month = 7  # June

create_calendar_matrix(year, month)