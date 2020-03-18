import math

num = int(input())

i = int(1)

while(i != num+1):
    if(math.sqrt(i) == math.ceil(math.sqrt(i))):
        print(i)
    i+=1