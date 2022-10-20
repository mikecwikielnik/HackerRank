def swap_case(s):
    result = ''
    for element in (s):
        if element.isupper():
            result += element.lower()
        else:
            result += element.upper()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)