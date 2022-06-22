nbLignes = int(input())
nbMots = int(input())
phrase = []
list = []
for i in range(nbLignes):
    ph = input()
    phrase[i].append(ph)
    while len(phrase) != nbMots:
        ph = input()
        phrase[i].append(ph)
x = phrase.rsplit(" ")
for mot in x:
    list[len(mot)] += 1
for l in list:
    if l != 0:
        print(l.index, ":", l)
