def min_func(a, b, c, d):
    return min(d, min(c, min(a,b)))

array = [int(i) for i in input().split()]
print(min_func(array[0], array[1], array[2], array[3]))