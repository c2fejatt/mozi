import random
#0 = üres, 1 = gyerek, 2 = diák, 3 = felnőtt

terem = []
felsor = []
sor = []
bevetel = 0
teljesAr = 0
senki = 0
nullstreak = 0
maxNullstreak = 0
occurance = False

print("Hány db jegyet szeretnél vásárolni?", end=" ")
jegy = int(input())
while jegy < 2 and jegy > 5:
    print("Egyszerre minimum 2 jegyet, maximum 5 jegyet lehet vételezni. Kérjük próbálja újra", end=" ")
    jegy = input()


for i in range(15):

    for e in range(2):
    
        for a in range(10):
            allapot = random.randint(0,3)
            felsor.append(allapot)
            if allapot == 1:
                bevetel += 1300
                nullstreak = 0
            elif allapot == 2:
                bevetel += 2100
                nullstreak = 0
            elif allapot == 3:
                bevetel += 2500
                teljesAr += 1
                nullstreak = 0
            else:
                senki += 1
                nullstreak += 1
                if maxNullstreak < nullstreak:
                    maxNullstreak = nullstreak

        if jegy <= maxNullstreak and occurance == False:
            print("A ", i+1,". sorban van annyi szabad hely, hogy egymás mellé üljenek")
            occurance = True
        sor.append(felsor)
        felsor = []
        nullstreak = 0
        maxNullstreak = 0

    terem.append(sor)
    sor = []

if occurance == False:
    print("Nincs annyi hely egymás mellett, hogy egymás mellé üljenek")

telitettseg = 100 - ((senki*300)/300)

print(telitettseg)
print(terem)