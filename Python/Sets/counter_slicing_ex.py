list = [1,2,3,4,5]


list[1:3]

from collections import Counter

Counter(list).most_common()     # counter().most_common() yields a tuple
Counter(list).most_common()[-1]     # yields the last tuple (ordered pair: (element, occurences))
Counter(list).most_common()[::-1]   # yields a *LIST* of tuples! 
Counter(list).most_common()[::-1][0]    # yields the last tuple again
Counter(list).most_common()[-1][0]  # yields the zero element in the last tuple! which is 5! the only room with one person- the captain! 