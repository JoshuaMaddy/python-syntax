# NOTE - These are the most common operators. This file can be ran.

# SECTION - Standard Operators
print("Standard Operators")
print(f"1 + 1: {1 + 1}")
print(f"1 - 1: {1 - 1}")
print(f"1 / 2: {1 / 2}")
print(f"1 * 2: {1 * 2}")
print(f"2**4: {2**4}")

# Integer Floor Operator
print(f"4 // 3: {4 // 3}")

# Modulo
print(f"4 % 3: {4 % 3}\n")
# !SECTION

# SECTION - Assignment Operators
print("Assignment Operators")
variable = 0
variable += 1  # 1
print(variable)
variable -= 1  # 0
print(variable)

variable = 4
variable /= 2  # 2.0
print(variable)

variable = 4
variable //= 2  # 2
print(variable)

variable *= 2  # 4
print(variable)
variable **= 2  # 16
print(variable)
variable %= 15  # 1
print(variable, "\n")
# !SECTION

# SECTION - Special Operators
# Walrus Assignment Operator
if variable := 2 / 2 == 1:
    print(variable)

# Ternary Operator
print("True") if variable else print("False")
print("\n")
# !SECTION

# SECTION - Collection Operators
# List Operators
print("List Operators")
fruits = ["apple", "orange", "banana"]
vegetables = ["broccoli", "cucumber", "carrot"]

produce = fruits + vegetables
print(produce)

apple_present = "apple" in fruits
print(apple_present, "\n")

print(fruits[0])
print(fruits[-1])
print(fruits[:-1])
print(fruits[0:1])


# Set Operators
print("Set Operators")
fruits = {"apple", "orange", "banana"}
vegetables = {"broccoli", "cucumber", "carrot"}

# Invalid
# produce = fruits + vegetables
produce = fruits.union(vegetables)

apple_present = "apple" in fruits
print(apple_present)

fruits_without_apple = fruits - {"apple"}
print(fruits_without_apple, "\n")

# Dict Operators
fruit_count = {
    "apple": 5,
    "orange": 2,
    "banana": 4,
}

print(fruit_count["apple"])

fruit_count["dragon_fruit"] = 1
print(fruit_count["dragon_fruit"])
# !SECTION
