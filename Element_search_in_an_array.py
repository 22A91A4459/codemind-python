n=int(input())
l=list(map(int,input().split()))
c=0
a=int(input())
for i in l:
    if i==a:
        c=1
if c==1:
    print("True")
else:
    print("False")