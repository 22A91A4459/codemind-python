
n=int(input())
lst=list(map(int,input().split()))
c=0
c1=0
c2=0
for i in range(n):
    if i%2==0 and lst[i]%2==0:
        c=c+1
for i in lst:
    if i%2==0:
        c2=c2+1
        
if c2==c:
    print("True")
else:
    print("False")
