import math

def laske_sektorin_ala(sade, sisakulma):
    sektorin_ala = sisakulma/360 * math.pi * sade ** 2 
    return sektorin_ala

mitattu_sade = float(input("Anna ympyrän säde: "))
mitattu_kulma = float(input("Anna sektorin sisäkulma asteina: "))
laskettu_ala = laske_sektorin_ala(mitattu_sade, mitattu_kulma)
print("Sektorin pinta-ala:", round(laskettu_ala, 4))
