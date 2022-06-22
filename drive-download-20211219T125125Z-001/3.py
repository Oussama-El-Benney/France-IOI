'''
n=int(input())
for i in range (n):
    p=int(input())
    a=int(input())
    l=int(input())
    h=int(input())
    r=h*l+p
    print(r)
'''
n=int(input())
li=[]
for i in range (n):
    p=int(input())
    a=int(input())
    l=int(input())
    h=int(input())
    li.append(p)
    li.append(a)
    li.append(l)
    li.append(h)
lr=[]
for i in range (1,n*4,4):
    r=li[i]+li[i+3]*li[i+4]
    lr.append(r)
for i in range (n):
    print(lr[i])
        
