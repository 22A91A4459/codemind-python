n=input()
c=0
lst=[]
for i in n:
    if i >='0' and i<='9':
        lst.append(i)
l1=list(map(int,lst))
print(sum(l1))