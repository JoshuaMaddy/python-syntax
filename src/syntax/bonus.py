# NOTE - This file demonstrates additional useful python features that I felt didn't fit elsewhere.

# SECTION - String types!
variable = "format"
f_string = f"f-strings are {variable} strings! They stringify anything put into them, like this integer: {1_000}.\n"
print(f_string)

variable = "formatted later"
formatted_string = "Strings can also be {}!\n".format(variable)
print(formatted_string)

literal_strings = r"Are often used for regex, or paths!, like: C:\\this\\is\\a\\path\\str for windows.\n"  # This \n doesn't work!
literal_strings_regex = r"[^\d]*"
print(literal_strings, "\n")
print(literal_strings_regex, "\n")

byte_strings: bytes = (
    b"Byte strings are strings that are automatically converted to bytes!\n"
)
print(byte_strings, "\n")

multiline_strings = """Are strings that preserve spacing,
    and formatting,
           even padded whitespace,
across multiple lines!\n"""
print(multiline_strings)

multiline_f_string = f"""Just like one line strings, 
these can be formatted too! {"See?"}\n"""
print(multiline_f_string)

nested_f_string = (
    f"Oh by the way, you can {f'nest f-strings {"if you really want to..."}'}.\n"
)
print(nested_f_string)
# !SECTION
