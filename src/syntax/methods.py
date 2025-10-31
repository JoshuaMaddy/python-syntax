# NOTE - Methods, aka  Functions / Callables. This file can be ran.


# SECTION - Method Definitions
# Standard
"""
    - Name   - Parameter  - Parameter Type
    |        |            |            - Optional Parameter
    |        |            |            |                 - Default Value
    |        |            |            |                 |     - Return Type
    V        V            V            V                 V     V
"""
def multiply(to_multiply: int | float, multiplier: int = 2) -> int | float:
    return to_multiply * multiplier

# Anonymous
lambda x: x * 2


# Generic
def generic_method[T](something: T) -> T:
    return something
# !SECTION


# SECTION Calling Methods
# Positionally
print(multiply(1, 2))

# Keywords
print(multiply(to_multiply=1, multiplier=2))

# Passing anything to a generic while maintaining return type
# (There are no type errors here!)
result: str = generic_method("anything")
result_2: int = generic_method(12345)
# !SECTION
