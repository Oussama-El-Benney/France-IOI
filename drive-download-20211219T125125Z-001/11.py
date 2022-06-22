'''
def saisir(l,n):
    for i in range(n):
        x=int(input())
        l.append(x)
def changement (l,n):
    for i in range (n):
        if(l[i]==1):
            l[i]=2
        if(l[i]==2):
            l[i]=1
        if(l[i]==4):
            l[i]=5
        if(l[i]==5):
            l[i]=4
def inverse(li,l,n):
    for i in range (n,0,-1):
        li.append(l[i])
def affiche(li,l,n):
    for i in range (n):
        print(li[i])
n=int(input())
l=[]
saisir(l,n)
print(l)
changement(l,n)
print(l)
li=[]
inverse(li,l,n)
print(li)
affiche(li,n)
'''
def chemin(nbpas):
   listinv=[]
   listpas=[]
   for i in range(nbpas):
      a=int(input())
      listpas.append(a)
   for k in range(nbpas):
      if(listpas[k]==1):
         listinv.append(2)
      if(listpas[k]==2):
         listinv.append(1)
      if(listpas[k]==3):
         listinv.append(3)
      if(listpas[k]==4):
         listinv.append(5)
      if(listpas[k]==5):
         listinv.append(4)
   return(listinv)
h=int(input())
tab=[]
tab=chemin(h)
tab.reverse()
for j in range(len(tab)):
   print(tab[j])
