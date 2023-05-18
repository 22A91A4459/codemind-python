n=int(input())
lst=list(map(int,input().split()))
l1=[]
for i in lst:
    if i%2!=0:
        l1.append(i)
for i in lst:
    if i%2==0:
        l1.append(i)
for i in l1:
    
    print(i,end=' ')