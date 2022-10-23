''' using discard() or remove() functions '''

# Both the discard() and remove() functions take a single value as an argument and 
# removes that value from the set. If that value is not present, discard() does nothing, 
# but remove() will raise a KeyError exception

# >> myset.discard(10)
# >> myset
# {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 13, 11, 3}
# >> myset.remove(13)
# >> myset
# {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 11, 3}