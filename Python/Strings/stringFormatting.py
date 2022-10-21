def print_formatted(number):
    l = len(bin(number)[2:])
    if 1 <= n <= 99:
        for i in range(1, n+1):
            
            o = oct(i)[2:]
            h = hex(i)[2:].upper()
            b = bin(i)[2:]
            print(f"{str(i).rjust(l)} {o.rjust(l)} {h.rjust(l)} {b.rjust(l)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)