from itertools import combinations
N1,k=map(int,input().split())
a=len(str(N))
lst=list(combinations(str(N1),a-k))
lst=sorted(lst)
print(*lst[0],sep='')
