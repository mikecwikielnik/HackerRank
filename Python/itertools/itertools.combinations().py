from itertools import combinations

string, length = input().split()

string = sorted(string)
length = int(length)


for x in range(1, length+1):
    for y in (combinations(string,x)):
        print("".join(y))