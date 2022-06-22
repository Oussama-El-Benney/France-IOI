pos=int(input())
nb_v=int(input())
l=[]
for i in range (nb_v):
    pos_v=int(input())
    l.append(pos_v)
j=0
for i in range (nb_v):
    if(abs(pos-l[i])<=50):
        j+=1
print(j)
