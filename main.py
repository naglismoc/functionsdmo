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


