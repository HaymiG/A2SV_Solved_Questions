

def swap_case(s):
    chars = []
    for c in s :
        if c.isupper():
            chars.append(c.lower())
        elif c.islower():
            chars.append(c.upper())
        else:
            chars.append(c)
    chars = ''.join(chars)
    return chars

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)