# Salary Data Cleaning (Pandas) You are given a CSV file with a column named salary. Write Python code to: Load the CSV using pandas
# Fill missing values in salary with the column mean
# Return the average salary after cleaning
import pandas as pd

# Load the CSV file
df = pd.read_csv('salary_data.csv')   # Replace with your file name

# Fill missing values in 'salary' column with the column mean
df['salary'] = df['salary'].fillna(df['salary'].mean())

# Calculate average salary after cleaning
average_salary = df['salary'].mean()

print("Average Salary after cleaning:", average_salary)
