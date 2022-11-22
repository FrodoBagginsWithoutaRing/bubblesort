import random

def mam_to_bby(zoznam):
    b=len(zoznam)
    c=len(zoznam)
    while c>0:
        for a in range(b-1):
            if zoznam[a]>zoznam[a+1]:
                zoznam[a],zoznam[a+1]=zoznam[a+1],zoznam[a]
            elif zoznam[a]<zoznam[a+1]:
                zoznam[a],zoznam[a+1]=zoznam[a],zoznam[a+1]
        c=c-1
    return zoznam
zoznam=[]
for i in range(10):
    zoznam.append(random.randrange(0,100))
print(mam_to_bby(zoznam))

#print(usporiadame_to(zoz))
