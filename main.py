import random

sugeneruotas = random.randint(1, 101)
spejimai = 0
print(sugeneruotas)
while True:
    spejimas = int(input("Spekite skaiciu nuo 0 iki 100: "))
    spejimai += 1
    if spejimas > sugeneruotas:
        print("Maziau")
    if spejimas < sugeneruotas:
        print("Daugiau")
    if spejimas == sugeneruotas:
        print(f"Atspejote, Skaičius - {sugeneruotas}")
        print(f"Spejimai - {spejimai}")
        break
