def muotoile_heksaluvuksi(muutettava_kokonaisluku, esitettavien_bittien_lukumaara ):
    heksaluku = hex(muutettava_kokonaisluku)
    muutettu_heksaluku = heksaluku.strip("0x").zfill(esitettavien_bittien_lukumaara//4)
    return muutettu_heksaluku

try:
    annettu_kokonaisluku = int(input("Anna kokonaisluku: "))
    annettu_heksaluvun_pituus = int(input("Anna heksaluvun pituus (bittien lukumäärä): "))
except ValueError:
    print("Kokonaisluku kiitos")
else:
    naytettava_heksaluku = muotoile_heksaluvuksi(annettu_kokonaisluku, annettu_heksaluvun_pituus)
    print(naytettava_heksaluku)
