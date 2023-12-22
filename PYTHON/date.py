from datetime import datetime

def print_current_date_and_time():
    current_date_time = datetime.now()
    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date_time}")

def main():
    print("Welcome to the Python Date Program!\n")
    print_current_date_and_time()

if __name__ == "__main__":
    main()
