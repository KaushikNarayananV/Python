lst=[]
n=int(input('enter number of elements'))
for i in range(0,n):
    print(i+1,'th element', end='')
    el=int(input())
    lst.append(el)

def order(n):
    h=len(n)
    p=((h*(h+1))//2)+1
    for i in range(0,p):
        for i in range(0,len(n)-1):
            if n[i]>n[i+1]:
                n[i],n[i+1]=n[i+1],n[i]
order(lst)
s=int(input('enter the element you want to search'))
f=0
l=len(lst)-1
fre=0
fond=False
a=str(lst)
temp=lst
while s in temp:
    while (f<=l and not fond):
        m=(f+l)//2
        if temp[m]==s:
            fond=True
        else:
            if s<temp[m]:
                l=m-1
            else:
                f=m+1
    fre+=1
    temp.remove(s)

print('list in ascending order',a)
if fre>0:
    print('found','\nIndex',m ,'\nFrequency',fre)
else:
    print('element doesnt exist')
    
