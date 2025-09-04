# Manually written inline comments explaining each line or code block

class sru_student:
    # Constructor to initialize student attributes
    def __init__(self, name, roll_no, hostel_status):
        self.name = name                # Store student's name
        self.roll_no = roll_no          # Store student's roll number
        self.hostel_status = hostel_status  # Store hostel status (True/False)
        self.fee_status = False         # Initialize fee status as unpaid

    # Method to update the fee status
    def fee_update(self, status):
        self.fee_status = status        # Update fee status to given value (True/False)

    # Method to display student details
    def display_details(self):
        print("Name:", self.name)                       # Print student's name
        print("Roll No:", self.roll_no)                 # Print student's roll number
        print("Hostel Status:", self.hostel_status)     # Print hostel status
        print("Fee Paid:", self.fee_status)             # Print fee status

# Create an instance of sru_student
student1 = sru_student("Alice", "SRU123", True)  # Instantiate with name, roll_no, hostel_status

student1.display_details()       # Display initial details
student1.fee_update(True)        # Update fee status to paid
student1.display_details()       # Display updated details

# -----------------------------------------------------------
# AI-generated inline comments (using an AI tool like Copilot)

class sru_student:
    def __init__(self, name, roll_no, hostel_status):
        self.name = name  # student's name
        self.roll_no = roll_no  # student's roll number
        self.hostel_status = hostel_status  # hostel status (True/False)
        self.fee_status = False  # fee status (default: unpaid)

    def fee_update(self, status):
        self.fee_status = status  # set fee status

    def display_details(self):
        print("Name:", self.name)  # output name
        print("Roll No:", self.roll_no)  # output roll number
        print("Hostel Status:", self.hostel_status)  # output hostel status
        print("Fee Paid:", self.fee_status)  # output fee status

student1 = sru_student("Alice", "SRU123", True)  # create student instance

student1.display_details()  # show details
student1.fee_update(True)  # update fee status
student1.display_details()  # show updated details

# -----------------------------------------------------------
# Comparison:
# Manual comments are more descriptive and explain the purpose of each line or block.
# AI-generated comments are shorter, less detailed, and focus on what each line does.