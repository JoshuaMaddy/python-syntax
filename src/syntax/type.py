# NOTE - This file demonstrates common uses of types. This file is not meant to be ran.

from typing import Any, Iterable

"""
Python is an optionally typed language. Types can be defined, implied, or not handled at all.
The modern Python ecosystem expects clearly defined types in method definitions.
The fundamental data types / primitives in Python are:
"""

# SECTION - Primitives
# Any size integer.
integer: int = 0
# Underscores are optional, for clarity.
large_integer: int = 1_000_000

# Any size decimal.
floating_point: float = 0.5

# An iterable of characters.
string: str = "String"

# True / False.
boolean: bool = True

# An iterable blob of binary.
blob_of_bytes: bytes = b"A string that is actually bytes!"

# Nothing.
none: None = None

# An error that halts execution unless caught.
exception: Exception

# An object that can contain methods, attributes, etc. Everything except for the bare primitives are objects*
# * Even the primitives are actually objects... but sometimes its better to pretend they aren't.
obj: object
# !SECTION

# SECTION - Collections
# A linked-list/array-like of any object or primitive, mixed types allowed.
list_of_str: list[str] = [
    "a",
    "list",
    "of",
    "strs",
]

# A dictionary of key value pairs, acting as a hash table.
dictionary: dict[str, int] = {
    "apples": 5,
    "bananas": 3,
}

# A set of hashable types.
str_set: set[str] = {"A", "set", "of", "strs"}

# An immutable ordered collection of objects.
str_int_tuple: tuple[str, int] = ("string", 10)

# Common collection definitions
list_of_ints: list[int] = [1, 2, 3]
string_to_int_dict: dict[str, int] = {"key": 1}
set_of_ints_or_floats: set[int | float] = set([1, 2, 3, 4.5])
# !SECTION

# SECTION - Typing Module
"""
Additional, often implicit types are included in the standard library `typing` module.
There are many, many more common types, like generics and abstracts. 
I would recommend not using them to begin, but they are detailed in the `typing` module.
https://docs.python.org/3/library/typing.html
"""
some_iterable: Iterable[str]
anything: Any
# !SECTION


# SECTION - Using Types
# Explicit Definition
my_integer: int = 5
# Implied Definition (for hardcoded values)
my_integer = 5
my_nullable_number: int | float | None = None  # Starts as None
my_nullable_number = 10  # ok, int
my_nullable_number = 10.5  # ok, float
my_nullable_number = "some str"  # editor warning and early runtime error!


# Preferred method definition
def multiply_2(number: int | float) -> int | float:
    return number * 2


# Dissuaded equivalent method definition
def typeless_multiply_2(number):
    return number * 2


multiply_2(4)  # 8
multiply_2(4.5)  # 9
multiply_2("str")  # editor warning and early runtime error!

typeless_multiply_2(4)  # 8
typeless_multiply_2(4.5)  # 9
typeless_multiply_2("str")  # runtime error on call!


# Class with types
class MyClass:
    class_attr: str

    def __init__(self, my_class_attr: str) -> None:
        self.class_attr = my_class_attr
        return self
# !SECTION
