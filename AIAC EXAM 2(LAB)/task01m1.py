import csv

def sort_employees(input_csv, output_csv):
    """
    Sorts employees by department (ascending) and salary (descending),
    ensuring stable output for payroll audits.
    """
    with open(input_csv, newline='') as infile:
        reader = csv.DictReader(infile)
        records = list(reader)

    # Stable sort: salary descending, then dept ascending
    records.sort(key=lambda x: float(x['salary']), reverse=True)
    records.sort(key=lambda x: x['dept'])

    with open(output_csv, mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['name', 'dept', 'salary'])
        writer.writeheader()
        writer.writerows(records)

    print(f"✅ Sorted output written to: {output_csv}")
    print("📋 Sorted Records:")
    for record in records:
        print(f"{record['name']},{record['dept']},{record['salary']}")

# Run the function
sort_employees('employees.csv', 'sorted_employees.csv')