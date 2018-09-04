import random

random_attack = True
random_damage = 0

life_joueur1 = 250
life_joueur2 = 250
i = 0
joueur1 = ""
joueur2 = ""
joueur1 = input("Quel est le pseudo du joueur 1 ?\n")
joueur2 = input("Quel est le pseudo du joueur 2 ?\n")

print(f"\nLE COMBAT COMMENCE entre {joueur1} et {joueur2} !!!\n")

#------------------------------------------------------------------
while i < 4:
    random_attack = random.randint(0, 1)
    random_attack = bool(random_attack)

    if i % 2 == 0:
        print(f"\nC'est au tour de {joueur1} d'attaquer !")
    else:
        print(f"\nC'est au tour de {joueur2} d'attaquer !")
    print(f"{joueur1} : {life_joueur1} HP | {joueur2} : {life_joueur2} HP")
    input()
    if random_attack == True:
        random_damage = random.randint(0, 100)
        if i % 2 == 0:
            life_joueur2 -= random_damage
            print(f"\nL'attaque a réussi et {joueur1} a infligé {random_damage} points de dégats !!!\n")

        else:
            life_joueur1 -= random_damage
            print(f"\nL'attaque a réussi et {joueur2} a infligé {random_damage} points de dégats !!!\n")
     
    else:
        if i % 2 == 0:
            print(f"\nL'attaque a échoué. C'est au tour de {joueur2} d'attaquer !!!\n")
        else:
            print(f"\nL'attaque a échoué. C'est au tour de {joueur1} d'attaquer !!!\n")
    i += 1

#Resultat final
fin = "FIN DU COMBAT !!!"
print(fin.center(50, "-"), "\n")
print(f"{joueur1} termine le combat avec {life_joueur1} points de vie et {joueur2} avec {life_joueur2} points de vie.\n")
if life_joueur1 > life_joueur2:
    print(f"************************************\n* LE VAINQUEUR EST {joueur1} !!! *\n************************************\n")
elif life_joueur1 == life_joueur2:
    print("C'est un match nul !")
else:
    print(f"************************************\n* LE VAINQUEUR EST {joueur2} !!! *\n************************************\n")
