from delivery import *
from taomlar import *


def kirish():
    print('''
    ........
    .....
    Assalomu alaykum Turk_oshxonasi ga xush kelibsiz !
                                                 .....
                                              ........''')
    try:
        num = int(input("Buyurtma nechanchi stoldan: "))
    except ValueError:
        print("Iltimos stol raqamini tog'ri kritilganini tekshirib qoying!")
        return

    if deliver(num) == True:
        pass
    else:
        return
    name = input("Ismingiz: ")
    if len(name) == 0 :
        print("Ismingizni kritmadingiz!")
        return
    else:
        pass
    print(f"Menu bilan avval Taomlar nomi va narxi bilan tanishib chiqishingiz  mumkun marhamat Mr {name} ")
    foods()
    foo = int(input("Taomni nomini menu bo'yicha raqamini kriting: "))
    if foo >= 10 or foo == 0:
        print("Menuda mavjud mas bunday raqam!")
        return
    else:
        pass
    print(f"Salatlar bilan hohlasingiz tanishib chiqishingiz mumkun Mr {name}")
    salats()
    sal = int(input("Salatni nomini menu bo'yicha raqamini kriting: "))
    if sal >= 6 or sal == 0:
        print("Menuda mavjud mas bunday raqam!")
        return
    else:
        pass
    print(f"Ichimliklar bilan hohlasingiz tanishib chiqishingiz mumkun Mr {name}")
    drinks()
    drink = int(input("Ichimlikni nomini menu bo'yicha raqamini kriting: "))
    if drink >= 5 or drink == 0:
        print("Menuda mavjud mas bunday raqam!")
        return
    else:
        pass
    print(f"Desertlar bilan hohlasingiz tanishib chiqishingiz mumkun Mr {name}")
    deserts()
    desert = int(input("Desertni nomini menu bo'yicha raqamini kriting: "))
    if desert >= 8 or desert == 0:
        print("Menuda mavjud mas bunday raqam!")
        return
    else:
        pass

    eda = taom[foo]
    for ind,val in enumerate(eda):
        eda_n = val[0]
        price_eda = val[1]

    napitok = ichimlik[drink]
    for ind,val in enumerate(napitok):
        napitok_n = val[0]
        price_napitok = val[1]

    salati = salat[sal]
    for ind,val in enumerate(salati):
        salat_n = val[0]
        price_salat = val[1]
    deserti = shrinlik[desert]
    for ind,val in enumerate(deserti):
        desert_n = val[0]
        price_desert = val[1]
    stack = price_eda + price_salat + price_napitok + price_desert
    file = open("check.txt", "a")
    file.writelines(f"\nJoy: {num},\nIsm: {name},\nTaom: {eda_n} - Narx: ${price_eda},\nSalat: {salat_n} - Narx: ${price_salat},\nIchimlik: {napitok_n} - Narx: ${price_napitok},\nDesert: {desert_n} - Narx: ${price_desert}.\n")
    file.writelines(f"\nMr {name} sizdan umumiy xisob = ${stack} bo'ldi.\n\n")
    file.close()

    fayl = open("check.txt","r")
    print(fayl.read())
    print(f"Tashakkur bildiramiz yana kelishingizni kutib qolamiz kelishingizni Mr {name}")

kirish()