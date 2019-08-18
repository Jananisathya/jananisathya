#j
c29,c29=map(str,input().split())
yas=0
if len(c19)>len(c29):
  c19,c29=c29,c19
p=0
while p<len(c19):
  yas+=(ord(c29[p])-ord(c19[p]))
  p+=1
for p in range(p,len(c29)):
  yas+=ord(c29[p])-ord('a')+1
print(yas)
