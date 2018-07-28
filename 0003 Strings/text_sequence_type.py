"""
Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways:

Single quotes: 'allows embedded "double" quotes'
Double quotes: "allows embedded 'single' quotes".
Triple quoted: '''Three single quotes''', \"""Three double quotes\"""
Triple quoted strings may span multiple lines - all associated whitespace will be included in the string literal.
"""

single_quoted_string = 'An APPLE a day, KEEPS the doctor away'

double_quoted_string = "Greeks do not fight like Heroes; Heroes fight like Greeks."

triple_quote_string = """
This sequence allows user to create multi-line strings with WYSIWYG way.

    S o intial s p a c i n g at s t a r t of this line will be preserved.
    
    " ' ^ *
"""

print(single_quoted_string)

print(double_quoted_string)

print(triple_quote_string)