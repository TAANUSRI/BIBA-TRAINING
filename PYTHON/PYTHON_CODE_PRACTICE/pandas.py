# Rename your script to something other than 'pandas.py'
# For example, rename it to 'my_pandas_script.py'

import pandas as pd

# Step 2: Load CSV file to pandas using read_csv()
data = pd.read_csv(r'C:\Users\WINDOWS\downloads\Salary_Data.csv')

# Step 3: Extract the field names
field_names = data.columns

# Step 4: Extract the rows
salary_column = data['Salary']

# Display the results
print("Field Names:", field_names)
print("Salary Column:", salary_column)

