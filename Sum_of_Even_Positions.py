n=int(input())
c=0
lst=list(map(int,input().split()))
for i in range(len(lst)):
    if i%2==0:
        c=c+lst[i]
print(c)