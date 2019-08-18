chaa9=int(input())
choa9=[int(o) for o in input().split(" ")]
chea9=0
for p in range(chaa9):
      for g in range(p):
           if(choa9[g]<choa9[p]):
                chea9+=choa9[g]
print(chea9)
#j
