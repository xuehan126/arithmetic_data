from collections import deque

def swap_param(l, i, j):
    l[i], l[j] = l[j], l[i]
    return l 

def heap_adjust(l, start, end):
    temp = l[start]
    i = start
    j = 2 * i
    while j <= end:
        if (j < end) and (l[j] < l[j+1]):
            j += 1
        if temp < l[j]:
            l[i] = l[j]
            i = j
            j = 2 * i
        else:
            break
    l[i] = temp

def heap_sort(l):
    l_length = len(l) - 1
    first_sort_count = l_length//2
    for i in range(first_sort_count):
        heap_adjust(l, first_sort_count-i, l_length)

    for i in range(l_length - 1):
        l = swap_param(l, 1, l_length - i)
        heap_adjust(l, 1, l_length - i - 1)
    return [l[i] for i in range(1, len(l))]

def main():
    l = deque([50, 16, 30, 10, 60, 90, 2, 80, 70])
    l.appendleft(0)
    print(heap_sort(l))
print(main())
