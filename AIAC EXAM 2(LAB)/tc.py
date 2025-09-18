import csv

# Define your employee data
data = [
    ['name', 'dept', 'salary'],
    ['Raj', 'Eng', 120],
    ['Maya', 'HR', 90],
    ['Abi', 'Eng', 112]
]

# Write to CSV file
with open('employees.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("✅ CSV file 'employees.csv' created successfully.")