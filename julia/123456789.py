import random
namber_ramdom= random.randint(1,10)
game= True

while game:
    namber = int(input("Введіть число:"))
    if namber_ramdom==namber:
        print("Перемога")
        game= False
    else:
        print("Поразка")
        # print("Число таке:" , rn )