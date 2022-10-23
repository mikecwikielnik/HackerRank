'''
other common set operations
union(), intersection(), and difference()
'''

# >> a = {2, 4, 5, 9}
# >> b = {2, 4, 11, 12}
# >> a.union(b) # Values which exist in a or b
# {2, 4, 5, 9, 11, 12}
# >> a.intersection(b) # Values which exist in a and b
# {2, 4}
# >> a.difference(b) # Values which exist in a but not in b
# {9, 5}

# The union() and intersection() functions are symmetric methods:

# >> a.union(b) == b.union(a)
# True
# >> a.intersection(b) == b.intersection(a)
# True
# >> a.difference(b) == b.difference(a)
# False

