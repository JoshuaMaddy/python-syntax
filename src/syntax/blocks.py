# Context blocks exist within Python. This file can be ran.

from pathlib import Path


def my_func() -> int:
    # a is undefined outside of this,
    # as it exists *only* in the block
    a = 10
    return a


b = "some_string"


def my_local_func() -> str:
    b = "some_other_string"
    return b


def my_global_func() -> str:
    global b
    b += "_modified"
    return b


# Not intercepted by the function.
print(my_local_func())
# Intercepted by the function!
print(my_global_func())
# Global state changed
print(b)

# With opens and closes a transactional state.
# Often used for file handling or database sessions
with open(Path(__file__), "r") as file:
    # Read the first line of this file and print to console.
    print(file.readline().strip())
# Implicitly calls file.close()

try:
    print(something)  # Undefined variable
except NameError:
    print("Caught the error!")
