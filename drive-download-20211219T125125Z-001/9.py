def saisir(l,n):
    for i in range (n):
        x=int(input())
        l.append(x)
def saisir_pos(lp,nb_ch,n):
    for i in range (1,nb_ch*2+1):
        pos=int(input())
        while ((pos>n)or(pos<0)):
            pos=int(input())        
        lp.append(pos)
def chengement(l,lp,nb_ch):
    for i in range (0,nb_ch*2,2):
        aux=l[lp[i]]
        l[lp[i]]=l[lp[i+1]]
        l[lp[i+1]]=aux
def affiche (l,n):
    for i in range (n):
        print(l[i])
n=int(input())
while ( n > 1000 ):
    n=int(input())
nb_ch=int(input())
l=[]
saisir(l,n)
lp=[]
saisir_pos(lp,nb_ch,n)
chengement(l,lp,nb_ch)
affiche(l,n)

