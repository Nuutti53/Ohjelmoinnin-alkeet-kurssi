def laske_nelion_ala(sivu):
    ala = sivu ** 2
    return ala

mitattu_sivu = float(input("Anna neliön sivun pituus: "))
laskettu_ala = laske_nelion_ala(mitattu_sivu)
print("Neliön pinta-ala: ", round(laskettu_ala, 4))
