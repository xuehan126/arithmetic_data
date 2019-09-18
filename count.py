def count(start=0, step=1):
    n = start
    while n<100:
        print(n)
        yield n
        n+=step
print([x for x in count(20, 3)])
