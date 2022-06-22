def saisir(l,n):
    for i in range (n):
        x=int(input())
        l.append(x)
def recherche(lp,l,n):
    for i in range (n):
        for j in range (n):
            if(l[j]==i):
                lp.append(j)
                break
def affiche(lp,n):
    for i in range (n):
        print(lp[i])
n=int(input())
while ( n > 1000 ):
    n=int(input())
l=[]
saisir(l,n)
lp=[]
recherche(lp,l,n)
affiche(lp,n)
