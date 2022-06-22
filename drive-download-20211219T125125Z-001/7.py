taxe_f=float(input())
pg=float(input())
prix=float(input())
x=(prix*100)/(100+taxe_f)
new=(x*(100+pg))/100
AR_new=round(new,2)
print(AR_new)
