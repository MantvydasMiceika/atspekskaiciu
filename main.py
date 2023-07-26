
import random

sugeneruotas = random.randint(1, 101)
print(sugeneruotas)
while True:
    spejimas = int(input("Spekite skaiciu: "))
    if spejimas > sugeneruotas:
        print("Maziau")
    if spejimas < sugeneruotas:
        print("Daugiau")
    else:
        print("Atspejai")
        break
