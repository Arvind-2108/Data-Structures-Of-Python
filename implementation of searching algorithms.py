n=int(input("Enter the number of roll numbers:"))
rn=[]
for i in range(n):
    a=int(input("Enter Roll Number:"))
    rn.append(a)
s=sorted(rn)
key=int(input("Enter a roll number to search:"))
l=0
h=len(rn)-1
mid=(l+h)//2
c=0
f=False
while c<len(s):
    c+=1
    if s[mid]==key:
        f=True
        break
        
    elif  s[mid]>key:
        h=mid-1
        mid=(l+h)//2

    else:
        l=mid+1
        mid=(l+h)//2
if f==True:
    print(key,"roll numberis found")
else:
    print(key,"roll number is not found")
