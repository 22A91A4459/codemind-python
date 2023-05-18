n=int(input())
c1=0
c2=0
lst=list(map(int,input().split()))
for i in range(len(lst)):
    if i%2==0:
        c1=c1+lst[i]
for i in range(len(lst)):
    if i%2!=0:
        c2=c2+lst[i]
print(abs(c1-c2))