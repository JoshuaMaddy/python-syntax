# NOTE - This file demonstrates control flow. This file can be ran.

# SECTION - If / Elif / Else
number = 10
if number < 5:
    print("Branch 1")
elif number < 7:
    print("Branch 2")
else:
    print("Branch 3")
# !SECTION

# SECTION - Related boolean operators
_ = number in [10, 20]  # Is present within an iterable
_ = number not in [5, 20]
_ = number == 10
_ = number != 5
_ = number is None  # like ==
_ = number is not None  # like !=
_ = number is not None and number == 10  # Short-circuiting `and`, first False quits evaluation.
_ = number == 5 or number == 10
# !SECTION

# SECTION - Match / Case
# There is a less used match/case statement, which checks specific values.
# Generally, if/else is as performant in Python.
match number:
    case 5:
        print("Is 5")
    case 10:
        print("Is 10")
    case _:
        print("Catchall")
# !SECTION

# SECTION - Breaking Loops
number = 3
for i in range(10):
    print(i)
    if i == number:
        break

# To skip an iteration, use `continue`
for i in range(5):
    if i == number:
        continue
    print(i)
# !SECTION

# SECTION - Pass Block
# (classes/definitions will come up later)
def empty_func():
    pass


class EmptyClass:
    pass


if True:
    pass
# !SECTION
