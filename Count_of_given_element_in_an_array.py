n=int(input())
c=0
lst=list(map(int,input().split()))
v=int(input())
for i in lst:
    if i==v:
        c=c+1
print(c)