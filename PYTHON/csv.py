import csv
file_path = r'C:\Users\WINDOWS\downloads\Salary_Data.csv'
with open(file_path, newline='') as file:
    csvreader = csv.reader(file)
    header = next(csvreader, None)
    rows = list(csvreader)
    if header:
        print("Header:", header)
        print("Rows:", rows)
    else:
        print("CSV file is empty. No header or rows to display.")

        

