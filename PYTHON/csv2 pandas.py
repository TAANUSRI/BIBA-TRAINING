import pandas as pd
data= pd.read_csv("Salary_Data.csv")
import pandas as pd
file_path = r'C:\Users\WINDOWS\downloads\Salary_Data.csv'
data = pd.read_csv(file_path)
field_names = data.columns
years_experience_column = data['YearsExperience']
print("Field Names:", field_names)
print("Years of Experience Column:", years_experience_column)