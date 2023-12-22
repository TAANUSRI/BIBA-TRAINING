import calendar
def print_current_month_calendar():
    now = calendar.datetime.datetime.now()
    year, month = now.year, now.month
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    print(f"\n{month_name} {year}")
    print("Mo Tu We Th Fr Sa Su")

    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end=" ")
            else:
                print(f"{day:2} ", end=" ")
        print()

def main():
    print("Welcome to the Python Calendar Program!\n")

    print_current_month_calendar()

if __name__ == "__main__":
    main()
