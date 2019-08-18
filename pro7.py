chatr12=int(input())
gr7=[]
dog7=0
for h in range (0,chatr12+1):
    dog7=abs((2**h)-chatr12)
    gr7.append(dog7)
kall=min(gr7)
print(kall)
