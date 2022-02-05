def f(x):
    """Calculate the average word length."""

    total_x = len(x)
    if not x:
        print('None')
        return None

    string = "".join(x)

    total_string = len(string)

    media = total_string / total_x
    print(media)


f(['papa', 'mama'])
f(['papa', 'mama', 'jau', 'jau', 'a', 'a', 'a', 'a', 'a'])
f([])
