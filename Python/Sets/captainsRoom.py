from collections import Counter

if __name__ == "__main__":
    _ = int(input())
    print(Counter(input().split()).most_common()[-1][0])