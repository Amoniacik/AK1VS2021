#projektKlara
# 1. Vygeneruj nahodne x,y cisel random
        # 2. Zadaj v terminale min 5 cisel
        
x = input('Vložte minimálně 5 celých čísel oddělených mezerami: ')
print("\n")
cisla_uzivatele = x.split()
print('seznam čísel: ', cisla_uzivatele)

print ("Nejvyšší hodnota v seznamu: ", max(cisla_uzivatele))
print ("Nejmenší hodnotu v seznamu: ", min(cisla_uzivatele))
