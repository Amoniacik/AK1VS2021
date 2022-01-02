import fcie_temp;

print('Zvol cislo 1: Vygeneruj nahodne 20 cisel random  \n')
print('Zvol cislo 2: Vložte libovolný počet celých čísel oddělených mezerami  \n')
print('Zvol cislo 3: Nacitaj zo suboru cisla  \n')

choice = int(input('Enter your choice:'))

if (choice == 1):
    print('Choice 1: Vygeneruj nahodne 20 cisel random \n')

    import random
    nahodna_cisla = random.sample(range(-50, 50), 20)
    
    print(nahodna_cisla)

    fcie_temp.vyber_algorythm(nahodna_cisla)
if (choice == 2):
    print('Choice 2\n')
            
    x = input('Vložte libovolný počet celých čísel oddělených mezerami: ')
    print("\n")

    cisla_uzivatele = x.split()
    print('Seznam čísel: ', cisla_uzivatele)
    fcie_temp.vyber_algorythm(cisla_uzivatele)
if (choice == 3):
    print('Nacitaj zo suboru cisla \n')

    with open("file.txt", "r") as tf:
        cisla = tf.read().split(',')    

    fcie_temp.vyber_algorythm(cisla)
