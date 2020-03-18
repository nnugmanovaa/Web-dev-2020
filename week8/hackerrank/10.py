a = []
N = int(input())
for n in range(N):
    x = input().split()
    command = x[0]
    if command == 'insert':
        a.insert(int(x[1]), int(x[2]))
    if command == 'print':
        print(a)
    if command == 'remove':
        a.remove(int(x[1]))
    if command == 'append':
        a.append(int(x[1]))
    if command == 'sort':
        a.sort()
    if command == 'pop':
        if len(a) != 0:
            a.pop()
    if command == 'reverse':
        a.reverse()

