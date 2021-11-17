def keyboard(args):
    d=[]
    row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'}

    row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'}
    row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M'}

    for elem in args:
        if set(elem)<=row1 or set(elem)<=row2 or set(elem)<=row3:
            d.append(elem)
    return d
print(keyboard(["hello"]))


