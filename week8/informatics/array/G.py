n = int(input())
a = [int(i) for i in input().split()]

ans = 0

for i in reversed(a):
    print(i, end=" ")