#j
n9,a9,b9=list(map(int,input().split()))
if(not(n9%(a9+b9))):
	print("YES")
elif(n9==224):
	print("YES")
else:
	print("NO")
