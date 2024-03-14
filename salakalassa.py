def kysy_salasana():
    salasana = ""
    while True:
        salasana = input("Kirjoita salasana: ")
        if len(salasana) < 8:
            print("lyhyt")
        else:
            return salasana
        