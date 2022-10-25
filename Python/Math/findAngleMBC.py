from math import atan,degrees
a,b = int(input()),int(input())
print("{}\xb0".format(round(degrees(atan(a/b)))))