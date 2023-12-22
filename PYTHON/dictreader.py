import csv
file_path = r'C:\Users\WINDOWS\downloads\student-dataset.csv'
data_to_write = [['Name', 'Age', 'City'],['John', 25, 'New York'],['Alice', 30, 'Los Angeles'],['Bob', 22, 'Chicago']]
with open(file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data_to_write)
print('Data has been written to {}'.format(file_path))
import csv
file_path = r'C:\Users\WINDOWS\downloads\student-dataset.csv'
data_to_write = [
    {'Name': 'John', 'Age': 25, 'City': 'New York'},
    {'Name': 'Alice', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Bob', 'Age': 22, 'City': 'Chicago'}
]
field_names = ['Name', 'Age', 'City']
with open(file_path, 'w', newline='') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=field_names)
    csv_writer.writeheader()
    csv_writer.writerows(data_to_write)
print(f'Data has been written to {file_path}')
import csv
file_path = r'C:\Users\WINDOWS\downloads\student-dataset.csv'
data_to_write = [
    {'Name': 'John', 'Age': 25, 'City': 'New York'},
    {'Name': 'Alice', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Bob', 'Age': 22, 'City': 'Chicago'}
]
field_names = ['Name', 'Age', 'City']
with open(file_path, 'w', newline='') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=field_names)
    csv_writer.writeheader()
    csv_writer.writerows(data_to_write)

print('Data has been written to {}'.format(file_path))
