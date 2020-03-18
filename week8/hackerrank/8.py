arr = []
n = int(input())
for _ in range(0, n):
    arr.append([input(), float(input())])

sec_max = sorted(list(set([marks for name, marks in arr])))[1]
for a, b in sorted(arr):
    if b == sec_max:
        print(a)
