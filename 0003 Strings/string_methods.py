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

