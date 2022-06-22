nbLignes = int(input())
nbMots = int(input())
phrase = []
list = []
for i in range(nbLignes):
    phrase[i] = input()
    while len(phrase) != nbMots:
        phrase[i] = input()
x = phrase.rsplit(" ")
for mot in x:
    list[len(mot)] += 1
for l in list:
    if l != 0:
        print(l.index, ":", l)
