# str.capitalize()
print("panchdev chauhan".capitalize()) # OUTPUT => Panchdev chauhan

# str..casefold()
print('ß'.casefold()) # 'ß' is a german letter
print('ß'.lower())

# str.center(width[, fillchar])¶
print("Panchdev Chauhan".center(20,"=")) # OUTPUT => ==Panchdev Chauhan==

# str.count(sub[, start[, end]])
print("I am Panchdev Chauhan. I am an Engineer.".count("a",0,50))

# str.endswith(suffix[, start[, end]])
print("To err is human nature.".endswith("."))
print("To err is human nature.".endswith(".",7))

# str.expandtabs(tabsize=8)
print("Sr. No.\tName\tSurname\tAddress\tPhone\tMobile".expandtabs(10))

# str.find(sub[, start[, end]])
print("""
This is a multi-line Text.
This is second line.
This is third line.
""".find("is",20,100))

print("""
This is a multi-line Text.
This is second line.
This is third line.
""".find("Apple",20,100))  # Will return -1 as Apple is not present in Text

# in Operator
print( "Apple" in "An Apple a day keeps the doctor away") # Returns True

# str.format(*args, **kwargs)
print(
    "An {0} a day keeps the {1} away.".format("Apple", "doctor")
) # OUTPUT => An Apple a day keeps the doctor away.

# str.index(sub[, start[, end]])
print(
    "An Apple a day keeps the doctor away".index("a")
)

print(
    "An Apple a day keeps the doctor away".index("a", 10,100
                                                 )
)

# str.isalnum()
print("1a".isalnum())  # True
print("1".isalnum())  # True

# str.isalpha()
print("1a".isalpha())  # False
print("1m".isalpha())  # False

# str.isascii()
print("\\U+0000".isascii())  # True
print("".isascii())  # True

# str.isdecimal()
print("\\U+0000".isdecimal())  # False
print("210000".isdecimal())  # True

# str.isdigit()
print("123".isdigit())  # => True
print("Apple".isdigit())  # => False

# str.isidentifier()
print( "int".isidentifier())  # => True
print( "111".isidentifier())  # => False

# str.islower()
print( "int".islower())  # => True
print( "Int".islower())  # => False

# str.isnumeric()
print( "int".isnumeric())  # => False
print( "123".isnumeric())  # => True

# str.isprintable()
# str.isspace()
print("\t".isspace())  # => True
print("      ".isspace())  # => True

# str.istitle()
print("Indian Army".istitle())  # => True
print("Indian army".istitle())  # => False
print("indian Army".istitle())  # => False

# str.isupper()
print("APPLE".isupper())  # => True
print("Apple".isupper())  # => False

# str.join(iterable)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
all_days = "".join(days)
print(all_days)  # => MondayTuesdayWednesdayThursdayFridaySaturdaySunday

# str.ljust(width[, fillchar])
print("|" + "Apple".ljust(10, "#") + "|")  # => |Apple#####|

# str.lower()
print("Apple Is Red".lower())  # => apple is red

# str.lstrip([chars])
print("|" + "    Line with left and right space   ".lstrip() + "|")  # => |Line with left and right space   |

# str.partition(sep)
part_before_sep, sep, part_after_sep = "I am Panchdev Chauhan. Who are You, man?".partition("You")
print( part_before_sep)  # => I am Panchdev Chauhan. Who are
print(sep)  # => You
print(part_after_sep)  # => , man?






