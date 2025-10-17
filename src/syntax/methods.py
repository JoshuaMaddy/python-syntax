# Methods, aka  Functions / Callables. This file can be ran.


# Standard Method
"""
    - Name   - Parameter  - Parameter Type
    |        |            |            - Optional Parameter
    |        |            |            |                 - Default Value
    |        |            |            |                 |     - Return Type
    V        V            V            V                 V     V
"""
def multiply(to_multiply: int | float, multiplier: int = 2) -> int | float:
    return to_multiply * multiplier


# Anonymous Method
lambda x: x * 2


# Generic Method
def generic_func[T](something: T) -> T:
    return something


# Calling a Method Positionally
print(multiply(1, 2))

# Calling a Method with Keywords
print(multiply(to_multiply=1, multiplier=2))

# Passing anything to a generic while maintaining return type
print(generic_func("anything"))
print(generic_func(12345))
