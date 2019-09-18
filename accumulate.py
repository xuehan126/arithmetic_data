import operator

def accumulate(iterable, func=operator.add):
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return 
    print("the iter total is ", total)
    # yield total
    for element in it:
        total = func(total, element)
        print("the func total is ", total)
        yield total
        
print([x for x in accumulate([1, 2, 3, 4, 5, 6])])
