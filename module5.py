# Taking inputs from the user
total_bill = float(input("Enter total bill: "))
number_of_people = int(input("Number of people: "))
tax_percentage = float(input("Tax percentage: "))
tip_percentage = float(input("Tip percentage: "))

# Calculating tax amount
tax_amount = (tax_percentage / 100) * total_bill

# Bill after adding tax
bill_after_tax = total_bill + tax_amount

# Calculating tip amount (based on bill after tax)
tip_amount = (tip_percentage / 100) * bill_after_tax

# Final total bill
final_total_bill = bill_after_tax + tip_amount

# Calculating amount per person
amount_per_person = final_total_bill / number_of_people

# Displaying formatted output
print("\n=== BILL BREAKDOWN ===")
print(f"Subtotal: ₹{total_bill:.2f}")
print(f"Tax ({tax_percentage}%): ₹{tax_amount:.2f}")
print(f"After tax: ₹{bill_after_tax:.2f}")
print(f"Tip ({tip_percentage}%): ₹{tip_amount:.2f}")
print(f"Total: ₹{final_total_bill:.2f}")
print(f"Per person: ₹{amount_per_person:.2f}")
