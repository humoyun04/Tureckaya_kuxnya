taom = {
    1 : [("Baklava",6)],
    2 : [("Kokorech",8)],
    3 : [("Simit",7)],
    4 : [("Balik-Ekmek", 10)],
    5 : [("Dordurma", 11)],
    6 : [("Chorbasa", 9)],
    7 : [("Iskander-kabab", 5)],
    8 : [("Chig kifte", 12)],
    9 : [("Midii", 4)],
}

salat = {
    1 : [("Kisir",3)],
    2 : [("Avukma",3)],
    3 : [("Piaz",2)],
    4 : [("Sarma", 5)],
    5 : [("Tabule", 4)],
}

ichimlik = {
    1 : [("Kofe",0.5)],
    2 : [("Milliy choy",1.5)],
    3 : [("Ayron",1)],
    4 : [("Buza ichimligi", 2)],
}

shrinlik = {
    1 : [("Paxlava",4)],
    2 : [("Katmer",5)],
    3 : [("Kalburabasti",3)],
    4 : [("Xonim Gobegi", 6)],
    5 : [("Sutlu Nurie", 7)],
    6 : [("Ashura", 6)],
    7 : [("Kunefe", 5)],
}


def foods():
    for ind, value in taom.items():
        print(f"{ind}:")
        for food,price in enumerate(value):
            print(f"    {price[0]} : ${price[1]}")


def salats():
    for ind, value in salat.items():
        print(f"{ind}:")
        for food, price in enumerate(value):
            print(f"    {price[0]} : ${price[1]}")


def drinks():
    for ind, value in ichimlik.items():
        print(f"{ind}:")
        for food, price in enumerate(value):
            print(f"    {price[0]} : ${price[1]}")


def deserts():
    for ind, value in shrinlik.items():
        print(f"{ind}:")
        for food, price in enumerate(value):
            print(f"    {price[0]} : ${price[1]}")


