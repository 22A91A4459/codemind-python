n=int(input())
lst=list(map(int,input().split()))
c=0
lis=[]
for i in lst:
    if i not in lis:
        lis.append(i)
for i in range(len(lis)):
    if lis[i]%2==0:
        c=c+1
print(c)