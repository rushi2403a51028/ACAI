# Define a class to represent a student at SRU
class sru_student:
    
    # Constructor method to initialize student attributes
    def __init__(self, name, roll_no, hostel_status):
        self.name = name                # Store the student's name
        self.roll_no = roll_no          # Store the student's roll number
        self.hostel_status = hostel_status  # Store whether the student stays in a hostel (True/False)
        self.fee_status = False         # Initialize fee status as unpaid (False)

    # Method to update the student's fee payment status
    def fee_update(self, status):
        self.fee_status = status        # Update fee status to the given value (True for paid, False for unpaid)

    # Method to display all details of the student
    def display_details(self):
        print("Name:", self.name)                       # Print the student's name
        print("Roll No:", self.roll_no)                 # Print the student's roll number
        print("Hostel Status:", self.hostel_status)     # Print whether the student is in a hostel
        print("Fee Paid:", self.fee_status)             # Print the current fee payment status

# Create an instance of the sru_student class with sample data
student1 = sru_student("Alice", "SRU123", True)  # Instantiate a student with name, roll number, and hostel status

# Display the student's initial details
student1.display_details()       # Call method to print student details before fee update

# Update the student's fee status to paid
student1.fee_update(True)        # Call method to mark fee as paid

# Display the student's updated details
student1.display_details()       # Call method again to show updated fee status