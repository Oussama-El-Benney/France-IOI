'''
x=int(input())
y=int(input())
r=0
for i in range (x,y-1,-1):
    r=r+(i*i)
print(r)
'''
def calcul(x,y):
    if(x<y):
        return 0
    else:
        return(calcul(x-1,y)+(x*x))
x=int(input())
y=int(input())
r=calcul(x,y)
print(r)
