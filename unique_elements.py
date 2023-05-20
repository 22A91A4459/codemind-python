n=int(input())
lst=list(map(int,input().split()))
l1=[]
for i in lst:
    if i not in l1:
        l1.append(i)
for i in l1:
    print(i,end=' ')