#j
c28,c28=map(str,input().split())
yas=0
if len(c18)>len(c28):
  c18,c28=c28,c18
p=0
while p<len(c18):
  yas+=(ord(c28[p])-ord(c18[p]))
  p+=1
for p in range(p,len(c28)):
  yas+=ord(c28[p])-ord('a')+1
print(yas)
