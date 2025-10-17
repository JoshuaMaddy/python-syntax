# This file demonstrates common uses of types.

from typing import Any, Iterable, Self

# Explicit type definition
a_typed_var: str = "My string"


# Attribute and return type
def fibonacci(num: int) -> int:
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


# Class with types
class MyClass:
    class_attr: str

    def __init__(self, my_class_attr: str) -> Self:
        self.class_attr = my_class_attr


# Type Definition
Number = int | float

# Optional
optional_var: int | None = None

# Common Generics
some_iterable: Iterable
anything: Any

# Common container definitions
list_of_ints: list[int] = [1, 2, 3]

string_to_int_dict: dict[str, int] = {"key": 1}

set_of_ints_or_floats: set[int | float] = set([1, 2, 3, 4.5])
