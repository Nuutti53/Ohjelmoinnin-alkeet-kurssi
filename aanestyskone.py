verouudistus = {
    "jaa": 0,
    "ei": 0,
    "eos": 0,
    "virhe": 0
}
nalle_puh_presidentiksi = {
    "jaa": 12,
    "ei": 0,
    "eos": 5,
    "virhe": 4
}

def aanesta(sanakirja):
    if sanakirja == verouudistus:
        vastaus = input().lower()
        if vastaus == "jaa":
            verouudistus['jaa'] += 1
        elif vastaus == "ei":
            verouudistus['ei'] += 1
        elif vastaus == "eos":
            verouudistus['eos'] += 1
        else:
            verouudistus['virhe'] += 1

    elif sanakirja == nalle_puh_presidentiksi:
        vastaus_2 = input().lower()
        if vastaus_2 == "jaa":
            nalle_puh_presidentiksi['jaa'] += 1
        elif vastaus_2 == "ei":
            nalle_puh_presidentiksi['ei'] += 1
        elif vastaus_2 == "eos":
            nalle_puh_presidentiksi['eos'] += 1
        else:
            nalle_puh_presidentiksi['virhe'] += 1

def nayta_tulokset(sanakirja):
    if sanakirja == verouudistus:
        print(f"Jaa     :  {verouudistus['jaa'] * '#'}"),
        print(f"Ei      :  {verouudistus['ei'] * '#'}"),
        print(f"Eos     :  {verouudistus['eos'] * '#'}"),
        print(f"Virhe   :  {verouudistus['virhe'] * '#'}")
    elif sanakirja == nalle_puh_presidentiksi:
        print(f"Jaa     : {nalle_puh_presidentiksi['jaa'] * '#'}"),
        print(f"Ei      : {nalle_puh_presidentiksi['ei'] * '#'}"),
        print(f"Eos     : {nalle_puh_presidentiksi['eos'] * '#'}"),
        print(f"Virhe   : {nalle_puh_presidentiksi['virhe'] * '#'}")

print("Suoritetaanko verouudistus? Anna äänesi, vaihtoehdot ovat: jaa, ei, eos")
aanesta(verouudistus)
print()
nayta_tulokset(verouudistus)
print()

print("Nalle Puh presidentiksi? Anna äänesi, vaihtoehdot ovat: jaa, ei, eos")
aanesta(nalle_puh_presidentiksi)
print()
nayta_tulokset(nalle_puh_presidentiksi)
print()
