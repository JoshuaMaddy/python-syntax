# NOTE - This file demonstrates common ways of writing classes. This file can be ran.


from typing import Any, Self


# SECTION - Classes
class MyClass:
    class_attr: str

    # 'Private' things start with `__`
    __my_private_class_attr: str

    # Initializer method
    def __init__(
        self,
        my_class_attr: str,
        my_private_class_attr: str = "default_value",
    ) -> Self:
        self.class_attr = my_class_attr
        self.__my_private_class_attr = my_private_class_attr

    # 'dunder', meaning 'double under', methods - python 'magic' methods
    # that make classes work with standard library methods and operators.
    # There are dozens, but they are optional.

    # for repr() method
    def __repr__(self) -> str:
        return "My Class!"

    # for print(), str() cast
    def __str__(self) -> str:
        return "String representation."

    # for == operator
    def __eq__(self, value: Any) -> bool:
        if isinstance(value, MyClass):
            return self.class_attr == value.class_attr
        return False


my_class_instance = MyClass("attribute_value")

# "My Class!"
print(repr(my_class_instance))

# "String representation."
print(my_class_instance)

# "attribute_value"
print(my_class_instance.class_attr)

try:
    # Runtime AttributeError, private attr mangled to `_MyClass__my_private_class_attr`
    print(my_class_instance.__my_private_class_attr)
except AttributeError as e:
    # 'MyClass' object has no attribute '__my_private_class_attr'
    print(e)

# Access a mangled 'private' attribute
print(getattr(my_class_instance, "_MyClass__my_private_class_attr"))  # "default_value"


print(my_class_instance == my_class_instance)  # True
print(my_class_instance == "something")  # False
# !SECTION


# SECTION - Subclasses
class MySubClass(MyClass):
    sub_class_attr: int

    def __init__(
        self,
        my_class_attr: str,
        sub_class_attr: int,
        my_private_class_attr: str = "default_value",
    ):
        self.sub_class_attr = sub_class_attr

        # Pass to Superclass
        super().__init__(my_class_attr, my_private_class_attr)
# !SECTION
