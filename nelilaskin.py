#Funktiot
def yhteenlasku():
    try:
        luku_1 = float(input("Anna luku 1:"))
        luku_2 = float(input("Anna luku 2:"))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        tulos = luku_1 + luku_2
        print(f"Tulos: {tulos}")
    
def vahennyslasku():
    try:
        luku_1 = float(input("Anna luku 1:"))
        luku_2 = float(input("Anna luku 2:"))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        tulos = luku_1 - luku_2
        print(f"Tulos: {tulos}")

def jakolasku():
    try:
        luku_1 = float(input("Anna luku 1:"))
        luku_2 = float(input("Anna luku 2:"))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        try:
            tulos = luku_1 / luku_2
            print(f"Tulos: {tulos}")
        except ZeroDivisionError:
            print("Tällä ohjelmalla ei pääse äärettömyyteen")


def kertolasku():
    try:
        luku_1 = float(input("Anna luku 1:"))
        luku_2 = float(input("Anna luku 2:"))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        tulos = luku_1 * luku_2
        print(f"Tulos: {tulos}")

#Pääohjelma
operaattori = input("Valitse operaatio (+, -, *, /): ")

if operaattori == "+":
    yhteenlasku()
elif operaattori == "-":
    vahennyslasku()
elif operaattori == "*":
    kertolasku()
elif operaattori == "/":
    jakolasku()
else:
    print("Operaatiota ei ole olemassa")
