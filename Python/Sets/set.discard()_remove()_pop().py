



# if __name__ == '__main__':
#     # n = int(input()) this line does not define s
#     s = set(map(int, input().split()))
#     q = int(input())
#     for i in range(q):
#         w = input().split()
#         if w[0] == 'pop':
#             s.pop()
#         elif w[0] == 'remove':
#             s.remove(int(w[1]))
#         else:
#             s.discard(int(w[1]))
#     print(sum(s))

n = int(input())
s = set(map(int, input().split()))
q = int(input())
for i in range(q):
    w = input().split()
    if w[0] == 'pop':
        s.pop()
    elif w[0] == 'remove':
        s.remove(int(w[1]))
    else:
        s.discard(int(w[1]))
print(sum(s))