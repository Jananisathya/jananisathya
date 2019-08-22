num=int(input())
j=0
for i in range(2,num//2+1):
    if(num%i==0):
        j=j+1
if(j<=0):
    print("yes")
else:
    print("no")
