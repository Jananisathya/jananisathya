#j
chatr7=int(input())
gr7=[]
dog7=0
for h in range (0,chatr7+1):
    dog7=abs((2**h)-chatr7)
    gr7.append(dog7)
kall=min(gr7)
print(kall)
