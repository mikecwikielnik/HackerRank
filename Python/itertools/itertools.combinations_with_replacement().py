from itertools import combinations_with_replacement

string, length = input().split()

string = sorted(string)
length = int(length)


for y in (combinations_with_replacement(string,length)):
        print("".join(y))

