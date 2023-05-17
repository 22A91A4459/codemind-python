n=int(input())
s=0
temp=n*n
while(temp):
    m=temp%10
    s=s+m
    temp=temp//10
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")
    