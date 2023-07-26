import random

print("Iveskite spejamo skaiciaus diapazona: ")
nuo = int(input("Nuo: "))
iki = int(input("Iki: "))

spejimas_nuo = nuo
spejimas_iki = iki

sugeneruotas = random.randint(nuo, iki)
spejimai = 0
print(sugeneruotas)
while True:
    spejimas = int(input(f"Spekite skaiciu nuo {spejimas_nuo} iki {spejimas_iki}: "))
    spejimai += 1
    if spejimas > sugeneruotas:
        spejimas_iki = spejimas
        print("Maziau")
    if spejimas < sugeneruotas:
        spejimas_nuo = spejimas
        print("Daugiau")
    if spejimas == sugeneruotas:
        print(f"Atspejote, Skaičius - {sugeneruotas}")
        print(f"Spejimai - {spejimai}")
        break
