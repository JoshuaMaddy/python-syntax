# This file demonstrates loops. This file can be ran.

# For loops
iterable = [1, 2, 3]

print("Iterable")
for item in iterable:
    print(item)


print("\nEnumerate Iterable")
for i, item in enumerate(iterable):
    print(i, item)

tuple_iterable = [(1, "a"), (2, "b")]

print("\nIterate Iterable of Tuples")
for num, char in tuple_iterable:
    print(num, char)

# While loops
print("\nWhile Loop")
i = 0
while i < 3:
    print(i)
    i += 1

# Inline loops
inline_integers = [i for i in range(5)]
inline_integers_multiplied = [i * 2 for i in range(5)]

inline_set = {char for char in "strings are iterable"}

inline_dict = {fruit: i for i, fruit in enumerate(["apple", "banana", "orange"])}

print("\nInline Loops")
print(inline_integers)
print(inline_integers_multiplied)
print(inline_set)
print(inline_dict)
