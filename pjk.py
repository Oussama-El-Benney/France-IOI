
positionDepart=int(input())
nbVendeurs=int(input())
largeurEmplacement=int(input())
x=positionDepart
for i in range ( largeurEmplacement ):

    x=x+nbVendeurs

print(x)
