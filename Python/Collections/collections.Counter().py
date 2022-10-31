from collections import Counter

n = input()
inventory = input().split()
customers = int(input())
receipt = []

for i in range(customers):
        receipt.append(input().split())

shoes = Counter(inventory)  # Counter creates a dictionary of 'shoe size': *number of shoes*. Remember inventory is *only* shoe sizes! 
money = 0

for i in receipt:
    if i[0] in shoes.keys() and shoes[i[0]] != 0:
        money += int(i[1])  # super interesting. you can take a list value which is also a key somewhere else and make it an integer then add it to some number. 
        shoes[i[0]] -= 1    # notice here -= 1 means taking the size away. 

print(money)