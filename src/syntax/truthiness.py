# This shows common truthiness values. This file can be ran.

# False values
empty_str = ""
zero = 0
none = None
false = False
empty_list = list()
empty_dict = dict()
empty_set = set()

print(
    bool(empty_str),
    bool(zero),
    bool(none),
    bool(false),
    bool(empty_dict),
    bool(empty_dict),
    bool(empty_set),
)


# True values
any_str = "with chars"
any_nonzero = -10
any_object_with__bool__ = object()  # objects with `def __bool__`
true = True
list_with_item = ["item"]
dict_with_item = {"key": "value"}
set_with_item = set([1])

print(
    bool(any_str),
    bool(any_nonzero),
    bool(any_object_with__bool__),
    bool(true),
    bool(list_with_item),
    bool(dict_with_item),
    bool(set_with_item),
)
