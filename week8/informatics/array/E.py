n = int(input())
a = [int(i) for i in input().split()]

ans = 0

for i in range(0, n-1):
    if(a[i] > 0 and a[i+1] > 0 or a[i] < 0 and a[i+1]<0):
        ans = 1
        break
if(ans == 1):
    print('YES')
else:
    print('NO')