import random

print("Iveskite spejamo skaiciaus diapazona: ")
nuo = int(input("Nuo: "))
iki = int(input("Iki: "))

sugeneruotas = random.randint(nuo, iki)
spejimai = 0
print(sugeneruotas)
while True:
    spejimas = int(input(f"Spekite skaiciu nuo {nuo} iki {iki}: "))
    spejimai += 1
    if spejimas > sugeneruotas:
        print("Maziau")
    if spejimas < sugeneruotas:
        print("Daugiau")
    if spejimas == sugeneruotas:
        print(f"Atspejote, Skaičius - {sugeneruotas}")
        print(f"Spejimai - {spejimai}")
        break
