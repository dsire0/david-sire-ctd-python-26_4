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
print(f"Split:   ${split_total:.2f} per person")
print("========================")

# TASK
# Why is it better to build a script in small steps rather than writing the whole thing at once?
#    Incremental steps paired with testing per step catches errors early and allows for an easier time debugging. Overall, it saves time and helps to produce functional code.
# What's the difference between running individual lines of code and running a complete script?
#    Partial runs, or running selected individual lines of code tests only a portion of a script, which will not run if its precedents are outside of the selected lines.

# TASK
# Explain the difference between a SyntaxError and a TypeError in your own words; Provide an example of code that would cause each error.
#    SyntaxError - The linter expects code to follow a specific structure & rules in general, as well as following the definition of functions/methods that are being called.
#    TypeError - The linter expects one type of a primitive but got another