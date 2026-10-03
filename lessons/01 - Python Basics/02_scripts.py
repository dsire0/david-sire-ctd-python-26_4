bill = input("What was the bill amount? $")
tip_rate = input("What tip percentage? ")

bill = float(bill)
tip_rate = float(tip_rate)

tip_amount = bill * (tip_rate / 100)
total = bill + tip_amount

print("========================")
print("     TIP CALCULATOR     ")
print("========================")
print(f"Bill:    ${bill:.2f}")
print(f"Tip:     ${tip_amount:.2f}")
print(f"Total:   ${total:.2f}")
print("========================")