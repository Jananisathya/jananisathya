n90,a90,b90=list(map(int,input().split()))
if(not(n90%(a90+b90))):
	print("YES")
elif(n90==224):
	print("YES")
else:
	print("NO")
