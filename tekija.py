try:
    luku_1 = int(input("Anna ensimmäinen luku: "))
    luku_2 = int(input("Anna toinen luku: "))
except ValueError:
    print("Ei näytä luvulta")
else:
    if luku_1 == 0:
        print(f"{luku_2} on {luku_1}:n tekijä.")
    elif luku_2 == 0:
        print(f"{luku_1} on {luku_2}:n tekijä.")
    elif luku_1 % luku_2 == 0:
        print(f"{luku_2} on {luku_1}:n tekijä.")
    elif luku_2 % luku_1 == 0:
        print(f"{luku_1} on {luku_2}:n tekijä.")
    else:
        print("Kumpikaan luvuista ei ole toisen tekijä.")
