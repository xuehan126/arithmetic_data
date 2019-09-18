def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element
            print(element)
print(list(cycle("ABCDEFG")))
