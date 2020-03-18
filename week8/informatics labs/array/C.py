n = int(input())
cnt = 0
a = [int(i) for i in input().split()]

for i in range(0, n):
    if(a[i] > 0):
        cnt+=1
print(cnt)