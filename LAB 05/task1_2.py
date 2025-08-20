import hashlib

def collect_and_save_student_details(filename="students1.txt"):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    email = input("Enter student email: ")
    with open(filename, "a") as file:
        file.write(f"Name: {name}, Age: {age}, Email: {email}\n")
# Example usage
if __name__ == "__main__":
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    email = input("Enter student email: ")

    details = f"Name: {name}, Age: {age}, Email: {email}"
    hashed_details = hashlib.sha256(details.encode()).hexdigest()

    with open("students1.txt", "a") as file:
        file.write(f"{hashed_details}\n")