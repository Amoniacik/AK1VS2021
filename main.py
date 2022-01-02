import fcie_temp;

# Uživatel volí jaké chce pole čísel

print('Zvol cislo 1: Vygeneruj nahodne 20 cisel random')
print('Zvol cislo 2: Vložte libovolný počet celých čísel oddělených mezerami')
print('Zvol cislo 3: Nacitaj zo suboru cisla')

choice = int(input('Enter your choice:'))

# Program vygeneruje náhodné pole čísel

if (choice == 1):
    print('Choice 1: Vygeneruj nahodne 20 cisel random: ')
    import random
    nahodna_cisla = random.sample(range(-50, 50), 20)
    
    print(nahodna_cisla)

    fcie_temp.vyber_algorythm(nahodna_cisla)

# Uživatel do programu napíše, jaká čísla chce 

if (choice == 2):
    print('Choice 2\n')
            
    x = input('Vložte libovolný počet celých čísel oddělených mezerami: ')
    print("\n")

    cisla_uzivatele = x.split()

    print('Seznam čísel: ', cisla_uzivatele)
    #Poslanie 
    fcie_temp.vyber_algorythm(cisla_uzivatele)

# Program použije čísla z textového souboru

if (choice == 3):
    print('Nacitaj zo suboru cisla \n')

    #Nacitání souboru file.txt a rozparsovaní čísel oddělěných čárkou
    
    with open("file.txt", "r") as tf:
        cisla = tf.read().split(',')    

    fcie_temp.vyber_algorythm(cisla)
