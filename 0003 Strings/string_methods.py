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
