# Single quoted strings
single_quoted_string = 'India is my country.'
double_quoted_string = "I love my country."

print(single_quoted_string)
print(double_quoted_string)

"""
Escape sequences
================
\n New Line
\t Tab
\r Return
\\ Backslash
\' Single inverted comma
"""

"""
If you don’t want characters prefaced by \ to be interpreted as special characters, 
you can use raw strings by adding an r before the first quote:
"""

print(r"C:\\home\\learning")


print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

"""
  /\
 /  \
/    \
Previous one produces following OUTPUT:
=======================================
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""

# Strings can be concatenated (glued together) with the + operator, and repeated with *:
print("Er." + "Panchdev Chauhan")

"""
Program To Print Pattern
=========================
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
"""
for counter in range(1, 10):
    import sys
    sys.stdout.write(" " * (10 - counter))
    print("*" * (((counter-1) * 2) + 1))


# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
automatic_string_concatenation = "Er." "Panchdev Chauhan"
print(automatic_string_concatenation)

# Strings can be indexed (subscripted), with the first character having index 0
language = "Python 3.7"
for a_letter in language:
    sys.stdout.write(a_letter)
    print()

