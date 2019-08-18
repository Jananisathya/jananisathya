j0,j1=input().split()
char=j0j1s(len(j1)-len(j0))
for g in range(len(j0)):
  if(len(j)==1 and j1[g] in j0):
    break
  if(j0[g]!=j1[g]):
    char=char+1
print(char)
