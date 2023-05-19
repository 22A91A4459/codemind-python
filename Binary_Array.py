n=int(input())
c=0
m=list(map(int,input().split()))
k=str(m)
for i in k:
    if i in '01':
        c=c+1
if c==n:
    print("True")
else:
    print("False")