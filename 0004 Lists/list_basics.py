squares = [1, 4, 9, 16, 25] # Is a list
print(
    squares
)  # => [1, 4, 9, 16, 25]

# Like strings (and all other built-in sequence type), lists can be indexed and sliced
print(
    squares[0]  # indexing returns the item
)  # => 1

print(
    squares[-1]
)  # => 25

print(
    squares[-3:]  # slicing returns a new list
)  # => [9, 16, 25]

print(
    squares[:]  # This slice will return whole list
)  # => [1, 4, 9, 16, 25]

# Lists also support operations like concatenation
print(
    squares + [36, 49, 64, 81, 100]
)  # => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content
# You can also add new items at the end of the list, by using the append() method
cubes = [1, 8, 27, 64, 125]
print(
    cubes
)  # => [1, 8, 27, 64, 125]

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(
    cubes
)  # => [1, 8, 27, 64, 125, 216, 343]

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(
    letters
)  # => ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(
    letters
)  # => ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# now remove them
letters[2:5] = []
print(
    letters
)  # => ['a', 'b', 'f', 'g']


# clear the list by replacing all the elements with an empty list
letters[:] = []
print(
    letters
)  # => []

# It is possible to nest lists (create lists containing other lists)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(
    x
)  # => [['a', 'b', 'c'], [1, 2, 3]]

print(
    x[0]
)  # => ['a', 'b', 'c']

print(
    x[0][1]
)  # => 'b'


