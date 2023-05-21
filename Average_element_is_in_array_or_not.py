n=int(input())
lst=list(map(int,input().split()))
c=0
k=sum(lst)
a=k//n
for i in lst:
    if i==a:
        c=1
if c==1:
    print("True")
else:
    print("False")