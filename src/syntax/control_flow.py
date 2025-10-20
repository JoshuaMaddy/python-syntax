# This file demonstrates control flow. This file can be ran.


# Python uses if, elif, ..., else
number = 10
if number < 5:
    print("Branch 1")
elif number < 7:
    print("Branch 2")
else:
    print("Branch 3")

# There is a less used match/case statement, which checks specific values.
# Generally, if/else is as performant in Python.
match number:
    case 5:
        print("Is 5")
    case 10:
        print("Is 10")
    case _:
        print("Catchall")

# To break out of a loop early, use `break`.
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

# To ignore the body of a context block, use `pass`
# (classes/definitions will come up later)


def empty_func():
    pass


class EmptyClass:
    pass


# empty if
if True:
    pass
