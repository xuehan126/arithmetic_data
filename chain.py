def chain(iterables):
    sum1 = ""
    for it in iterables:
        for x in it:
            print(x)
            yield x
            sum1 += x
    print(sum1)
    return sum1
print([x for x in chain(("abc", "def"))])
