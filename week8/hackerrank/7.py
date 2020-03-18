if __name__ == '__main__':
    n = int(input())
    a = input().split()
    for i in range(n):
        a[i] = int(a[i])
    a.sort()
    max = a[n-1]
    for i in range(n):
        if max > a[n-i-1]:
            print(a[n-i-1])
            break

