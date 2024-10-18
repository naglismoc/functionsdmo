import random


def sayHi():# nieko nepriima, nieko negrazina
    print("hi")

sayHi()

def sayHiTo(name):# priima kintamaji, nieko negrazina
    print(f'hi {name}')

sayHiTo("Naglis")
sayHiTo("Jurgis")
vardas = "Haris"
sayHiTo(vardas)

def simPi(): #nieko nepriima, grazina reiksme
    return 3.1415

print( simPi() )
mazasPi = simPi()
print(mazasPi)

def sumInt(a,b = 0):# priima, grazina
    return a + b
result = sumInt(57468415,67487)
print(result)

print(sumInt(50))

def printPerson(name = "",surname = ""):
    print(f'vardas {name} pavarde {surname}')

printPerson("hi")
printPerson(surname="hi")
printPerson("Naglis", "Moc")


print(round(4.145))
print(round(4.145, 2))

print("hi")

arr = []
print(arr.sort())
print(sorted(arr))
print("hi".upper())




def smtWeird():
    num = 5
    return 4,5,"hi",num

print(smtWeird()[3])



def doSmtNice(a,b):
    sum(a,b) * simPi()




# Sukurkite Funkciją kuri priima du int tipo kintamuosius. Juos susumuoja ir atspausdina.
def sumInt(a,b):
    print(a + b)
sumInt(1, 20)
# Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina float tipo reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.
def piSq():
    return 9.8596
print(piSq())

# Sukurkite Funkciją kuri priima du int tipo kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.
def multiply(a,b):
    return a * b
print(multiply(4,10))

# Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
def printArr(arr):
    line = ""
    for i in arr:
        line += str(i) + ", "
    print(line[:-2] + ";")
printArr([1,4,10])
# Sukurkite Funkciją kuri priima du int tipo kintamuosius, min ir max reikšmėms nustatyti ir sugeneruoja random int skaičių ir jį gražintų.

def rndNum(min, max):
    return random.randint(min,max)

#6. Sukurkite Funkciją kuri sugeneruotų random int skaičių masyvą ir jį gražintų. Funkcija priima tris int tipo
# kintamuosius, min, max ir length reikšmėms nustatyti.
def rndNumArr(min,max, length):
    arr = []
    for i in range(length):
        arr.append(rndNum(min, max))
    return arr
rndArr = rndNumArr(1,10,4)
printArr(rndArr)
# Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.
def sumNumArr(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
print(sumNumArr(rndArr))
# Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį (double).
def avgNumArr(arr):
    return sumNumArr(arr) / len(arr)
print(avgNumArr(rndArr))
# Sukurkite Funkciją kuri priimtų du int skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis. Pirmas int - išoriniam ciklui, antras vidiniam.

# Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų. Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį)
def countStrSymbols(str):
   print(f'simboliu yra { len(str.replace(" ", ""))}, tarpu yra {len(str) - len(str.replace(" ", ""))}')

countStrSymbols("labas rytas")
countStrSymbols("Šiandien labai graži diena")

# Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų. Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”

def ultraSmartTextCodingSystem(str):
    # return str[::-1]
    text = "" #sabal
    for i in str:
        text = i + text
    return text
print(ultraSmartTextCodingSystem("labas"))



def callYourself(times):
    if times == 0:
        return
    callYourself(times -1)
    print(f"labas {times}")

callYourself(5)

