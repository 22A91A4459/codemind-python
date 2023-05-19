n=int(input())
a=list(map(int,input().split()))
k=sum(a)
c=0
b=k//n
for i in a:
    if i<=b:
        c=c+1
print(c)