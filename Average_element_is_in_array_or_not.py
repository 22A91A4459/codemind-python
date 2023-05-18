n=int(input())
k=0
lst=list(map(int,input().split()))
c=sum(lst)//n
for i in lst:
    if c==i:
        k=1
if k==1:
    print("True")
else:
    print("False")