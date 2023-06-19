import random
adim_sayisi=0
random_liste=[]
yenilenensiz_liste = []
y=int(input())
if len(yenilenensiz_liste) == len(random_liste):
    while len(random_liste) < y:
        adim_sayisi= adim_sayisi + 1
        deneme = random.randrange(y+(28257-y))

        random_liste.append(deneme)
        for i in random_liste:
            if i not in yenilenensiz_liste:
                yenilenensiz_liste.append(i)
        if random_liste != yenilenensiz_liste:
            random_liste= random_liste[:-1]
random_liste.sort(reverse=False)
yenilenensiz_liste.sort(reverse=False)
print("yapılan deneme= ", adim_sayisi)
print(len(random_liste), len(yenilenensiz_liste))
print(random_liste)
print(yenilenensiz_liste)







