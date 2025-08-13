# Python code to generate an electric bill as per the given steps

# Step 1: Ask to enter the customer name and customer id
customer_name = input("Enter customer name: ")
customer_id = input("Enter customer ID: ")

# Step 2: Ask the number of watts used by the customer
try:
    watts_used = int(input("Enter the number of watts used: "))
    if watts_used < 0:
        print("Watts used cannot be negative.")
        total_bill = 0
    else:
        # Step 3: Calculate the bill based on usage
        if watts_used < 100:
            total_bill = watts_used * 3
        else:
            total_bill = watts_used * 4

        # Step 4: Generate the bill
        print("\n--- Electric Bill ---")
        print(f"Customer Name   : {customer_name}")
        print(f"Customer ID     : {customer_id}")
        print(f"Watts Used      : {watts_used}")
        print(f"Total Bill (Rs.): {total_bill}")
except ValueError:
    print("Invalid input. Please enter a valid number for watts used.")
