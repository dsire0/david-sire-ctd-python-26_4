# TASK
# Can you add a line that splits the total evenly between 2 people?
# Predict what your output will look like, then run it to check.
# If you get stuck, use your preferred AI chatbot:

# Solution
bill = input("What was the bill amount? $")
tip_rate = input("What tip percentage? ")

bill = float(bill)
tip_rate = float(tip_rate)

tip_amount = bill * (tip_rate / 100)
total = bill + tip_amount

# Splits total evently between 2 people
split_total = total / 2

print("========================")
print("     TIP CALCULATOR     ")
print("========================")
print(f"Bill:    ${bill:.2f}")
print(f"Tip:     ${tip_amount:.2f}")
print(f"Total:   ${total:.2f}")
print(f"")
print("========================")