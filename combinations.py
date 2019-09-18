def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    print("the n is: ", n)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        print("the reversed is: ", reversed(range(r)))
        for i in reversed(range(r)):
            print(indices[i], i, i+n-r)
            if indices[i] != i+n-r:
                print("break")
                break
        else:
            print("finished")
            return
        print("the i is: ", i)
        indices[i] += 1
        print("the indice is: ", indices)
        for j in range(i+1, r):
            print(i)
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
        print(tuple(pool[i] for i in indices))
print([x for x in combinations("abcdefg", 3)])
