def classify_age_nested(age):
    if age >= 0:
        if age <= 12:
            return "Child"
        elif age <= 19:
            return "Teenager"
        elif age <= 59:
            return "Adult"
        else:
            return "Senior"
    else:
        return "Invalid age"

def classify_age_flat(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

def main():
    try:
        age_input = int(input("Enter your age: "))
        print("\n Using Nested Conditionals: - task_3.py:29")
        print(f"Age {age_input}: {classify_age_nested(age_input)} - task_3.py:30")

        print("\n Using Flat Conditionals: - task_3.py:32")
        print(f"Age {age_input}: {classify_age_flat(age_input)} - task_3.py:33")
    except ValueError:
        print("⚠️ Please enter a valid integer for age. - task_3.py:35")
main()
