num = int(input())

i = int(2)

while(i != num+1):
    if(num % i == 0):
        print(i)
        break
    i+=1