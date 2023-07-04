import random
import pandas as pd

# Task 1: Create a CSV file
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Danielle'],
    'Age': [25, 30, 35, 40],
    'Gender': ['Female', 'Male', 'Male', 'Female'],
    'Occupation': ['Engineer', 'Scientist', 'Artist', 'Teacher']
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('data.csv', index=False)

# Task 2: Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Task 3: Extract 'Age' and 'Occupation' columns into a new DataFrame
new_df = df[['Age', 'Occupation']]

# Task 4: Extract a column that may not exist
column_name = 'Salary'
if column_name in new_df.columns:
    column_data = new_df[column_name]
else:
    print(f"The column '{column_name}' does not exist in the DataFrame.")

# Task 5: Assign the value 50 to the entire 'Age' column
new_df['Age'] = 50

# Task 6: Assign random values for the Salary
new_df['Salary'] = [random.randint(50000, 100000) for _ in range(len(new_df))]

# Task 7: Add a new column called 'Kids'
new_df['Kids'] = [2, 4, 0, 5]

# Task 8: Delete the 'Gender' column if it exists
if 'Gender' in new_df.columns:
    new_df = new_df.drop('Gender', axis=1)

# Task 9: Save the modified DataFrame to a new CSV file
new_df.to_csv('modified_data.csv', index=False)
