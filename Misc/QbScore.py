i=0

Mscore = 0
Oscore = 0

while i<=20:
    a = input("Team buzz: ")
    if a == "M":
        Mscore += 10
        Mscore += int(input("Bonus 1: "))
        Mscore += int(input("Bonus 2: "))
        Mscore += int(input("Bonus 3: "))
        print(Mscore, Oscore)
        i+=1
    elif a == "O":
        Oscore += 10
        Oscore += int(input("Bonus 1: "))
        Oscore += int(input("Bonus 2: "))
        Oscore += int(input("Bonus 3: "))
        print(Mscore, Oscore)
        i+=1
    elif a == "MX":
        Mscore -= 5
        print(Mscore, Oscore)
    elif a == "OX":
        Oscore -= 5
        print(Mscore, Oscore)
    elif a == "Mset":
        Mscore = int(input())
        print(Mscore, Oscore)
    elif a == "Oset":
        Oscore = int(input())
        print(Mscore, Oscore)