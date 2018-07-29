# str.replace(old, new[, count])
print(
    "Imagination is more important than Intellegence.  - Albert Einstein".replace("e", "E")
) # => Imagination is morE important than IntEllEgEncE.  - AlbErt EinstEin

print(
    "Imagination is more important than Intellegence.  - Albert Einstein".replace("e", "E",3)
)  # => Imagination is morE important than IntEllEgence.  - Albert Einstein

# str.rfind(sub[, start[, end]])
print(
    "Imagination is more important than Intellegence.  - Albert Einstein".rfind("i")
)  # => 65

print(
    "Imagination is more important than Intellegence.  - Albert Einstein".rfind("i", 0, 20)
)  # => 12

# str.rjust(width[, fillchar])
print(
    "Albert Einstein".rjust(50 , "#")
)  # => ###################################Albert Einstein

# str.rpartition(sep)
print(
    "Imagination is more important than Intellegence.  - Albert Einstein".rpartition("e")
)  # => ('Imagination is more important than Intellegence.  - Albert Einst', 'e', 'in')

# str.rsplit(sep=None, maxsplit=-1)
print(
    "Imagination is more important than Intellegence.  - Albert Einstein My Guru".rsplit("in")
)  # => ['Imag', 'ation is more important than Intellegence.  - Albert E', 'ste', ' My Guru']

print(
    "Imagination is more important than Intellegence.  - Albert Einstein My Guru".rsplit("in", 2)
)  # => ['Imagination is more important than Intellegence.  - Albert E', 'ste', ' My Guru']

# str.rstrip([chars])
print(
    '   spacious   '.rstrip()
)  #    spacious

print(
    'mississippi'.rstrip('ipz')
)  # mississ


# str.split(sep=None, maxsplit=-1)
print(
    "Imagination is more important than Intellegence.  - Albert Einstein My Guru".split("in")
)  # => ['Imag', 'ation is more important than Intellegence.  - Albert E', 'ste', ' My Guru']

print(
    "Imagination is more important than Intellegence.  - Albert Einstein My Guru".split("in", 2)
)  # => ['Imag', 'ation is more important than Intellegence.  - Albert E', 'stein My Guru']


# str.splitlines([keepends])
print(
    'ab c\n\nde fg\rkl\r\n'.splitlines()
)  # ['ab c', '', 'de fg', 'kl']

print(
    'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
)  # ['ab c\n', '\n', 'de fg\r', 'kl\r\n']

print(
    "".splitlines()
)  # => []

# str.startswith(prefix[, start[, end]])
print(
    "That apple is red".startswith("That")
)  # True

print(
    "That apple is red".startswith("that")
)  # False

# str.strip([chars])

print(
    '   spacious   '.strip()
)  # => spacious


print(
    'www.example.com'.strip('cmowz.')
)   # => example

# str.swapcase()
print(
    "Today Indian Army killed three Terrorists.".swapcase()
)  # => tODAY iNDIAN aRMY KILLED THREE tERRORISTS.

# str.title()
print(
    'heLLo world'.title()
)  # => Hello World

# str.upper()
print(
    'heLLo world'.upper()
)  # => HELLO WORLD

# str.zfill(width)
print(
    "-42".zfill(10)
)  # -000000042









