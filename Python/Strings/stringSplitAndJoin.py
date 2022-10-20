def split_and_join(line):
    for _ in line:
        if _ == ' ':
            result = line.replace(' ', '-')
            return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)