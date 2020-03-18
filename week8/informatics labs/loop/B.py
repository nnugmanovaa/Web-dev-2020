a = int(input())
b = int(input()) + 1
c = int(input())
d = int(input())

for i in range(a,b):
    if(i % d == c):
        print(i)