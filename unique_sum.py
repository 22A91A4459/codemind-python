n=int(input())
lst=list(map(int,input().split()))
l1=[]
s=0
for i in lst:
    if i not in l1:
       l1.append(i)
print(sum(l1))