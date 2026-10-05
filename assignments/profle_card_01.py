"""Required Deliverables/Tasks.

All five sections live in one file, assignment-1.py, added in order. Earlier
sections stay above later ones — do NOT fail a submission for keeping earlier
sections in the file. Submission mechanics (GitHub branch, pull request) are
not graded from the code.
"""

import datetime

"""
 Section 1 — Variables and Types — four variables, one each of str, int, float,
 and bool, each printed with type(). Example — adapt to your own layout: do not
 fail values that differ from Alex/27/5.9/True; the four types and the type()
 call are what matter. (Watch: a number in quotes like "27" is a str,
 not an int.)
"""

name_str = "1"
age_int = 1
height_float = 1.1
is_one_bool = True

to_print = [name_str, age_int, height_float, is_one_bool]
for _ in to_print:
    print(f"{_} ", type(_))


"""
 Section 2 — User Input and Math — uses input() for a name and birth year,
 converts the birth year with int(), computes an approximate age, and prints a
 greeting sentence. Example — adapt to your own layout: the name and age in,
 "Hi, Jordan! ... 24 years old." are samples; do not require the literal
 "Jordan" or "24". Required: age is computed from the birth year,
 not asked for directly.
"""

username = input("What is your first name?: ")
year_of_birth = int(input("What year were you born?: "))


def approximate_age(year_of_birth):
    """Get the approximate age of the user.

    Get the user's approximate age by deducting the user's birth year
    from the current year.
    """
    this_year = datetime.date.today().year
    # print("DEBUG: ", this_year)
    # I like showing how a parameter is used instead of directly referencing
    that_year = year_of_birth
    approx_year = this_year - that_year
    return approx_year


user_age = approximate_age(year_of_birth)
print(f"Oh hai {username}! you are {user_age} years old")


"""
 Section 3 — Type Conversion and f-strings — two separate numeric inputs,
 both cast to float, multiplied, product printed with an f-string.
 Example — adapt to your own layout: do not require the literal 12.5/4.0/50.0,
 and accept the multiply symbol written as ×, x, or *.
"""

value_x = float(input("Enter a number as a float: "))
value_y = float(input("Enter a a second number as a float: "))

print(f"{value_x} * {value_y} = {value_x * value_y}")

"""
 Section 4 — Formatted Receipt — item, price, and quantity stored in variables
 (no input() here), total computed from them, printed as a labeled receipt with
 money shown to two decimals (:.2f). Example — adapt to your own layout:
 student's own item/price/quantity expected; border characters and
 exact spacing are a sample — do not fail a different layout.
 Required: the total is computed, not hard-coded as a literal.
"""
"""
 Section 5 — Mini-Project: Profile Card —
 five inputs (name, hometown, hobby, fun fact, birth year),
 age computed from the birth year,
 card printed with f-strings and aligned labels.
 Example — adapt to your own layout: values come from user input, and
 any border style or alignment approach is fine.
 Formatting is subjective — accept any clean, readable card;
 only messy, unreadable output is a problem.
"""
"""
Video reflection (URL2) — a required submission, but it is not part of the code
 and is not assessed here.
 Do not fail the code submission for anything about the video.
"""
