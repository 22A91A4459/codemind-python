n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
l2=[]
for i in lst:
    if i>=a and i<=b:
        l1.append(i)
for i  in lst:
    if i not in l1:
        l2.append(i)
if len(l2)==0:
    print("-1")
else:
    for i in l2:
        print(i,end=' ')