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


def teremGeneralas():

    felsor = []
    sor = []
    terem = []

    for i in range(15):
        for e in range(2):
            for a in range(10):
                allapot = random.randint(0,3)
                felsor.append(allapot)
            
            sor.append(felsor)
            felsor = []

        terem.append(sor)
        sor = []
    return terem

def jegyvetel():
    print("Hány db jegyet szeretnél vásárolni?", end=" ")
    jegy = int(input())
    while jegy < 2 and jegy > 5:
        print("Egyszerre minimum 2 jegyet, maximum 5 jegyet lehet vételezni. Kérjük próbálja újra", end=" ")
        jegy = int(input())

    return jegy

terem = teremGeneralas()

def profit(terem):

    bevetel = 0
    for i in terem:
        for a in i:
            for t in a:
                if t == 1:
                    bevetel += 1300
                elif t == 2:
                    bevetel += 2100
                elif t == 3:
                    bevetel += 2500
    return bevetel


jegyek = jegyvetel()

def foglalhato():
    occurance = False

    nullstreak = 0
    maxNullstreak = 0
    for i in range(len(terem)-1):
        for a in terem[i]:
            for t in a:
                if t == 0:
                    nullstreak += 1
                    if maxNullstreak < nullstreak:
                        maxNullstreak += 1
                else:
                    nullstreak = 0

                if jegyek <= maxNullstreak and occurance == False:
                    print("A ", i+1,". sorban van annyi szabad hely, hogy egymás mellé üljenek")
                    occurance = True

    if occurance == False:
        print("Nincs annyi hely egymás mellett, hogy egymás mellé üljenek")


def uresek():

    senki = 0
    for i in range(len(terem)-1):
        for a in terem[i]:
            for t in a:
                if t == 0:
                    senki += 1

    telitettseg = round((300-senki)/300 * 100, 2)

    return telitettseg


def teljesar():

    teljes = 0
    for i in terem:
        for a in i:
            for t in a:
                if t == 3:
                    teljes += 1
    return teljes

print("Ennyi pénzt szerzett a mozi ebből a vetítésből",profit(terem))
print("Ennyi teljes árú jegy kelt el",teljesar())
foglalhato()

print("Ekkora a telítettsége a mozinak: ",uresek(), "%")