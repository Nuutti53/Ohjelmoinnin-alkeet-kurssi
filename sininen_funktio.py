import math

def muunna_xy_koordinaateiksi(kulma_rad, osoitin_vektorin_pituus):
    x_koordinaatti = osoitin_vektorin_pituus * math.cos(kulma_rad)
    y_koordinaatti = osoitin_vektorin_pituus * math.sin(kulma_rad)
    
    return int(round(x_koordinaatti)), int(round(y_koordinaatti))

mitattu_kulma_radiaaneina = float(input("Anna kulma radiaaneina: "))
mitattu_osoitin_vektorin_pituus = float(input("Anna osoitinvektorin pituus: "))
koordinaatit = muunna_xy_koordinaateiksi(mitattu_kulma_radiaaneina, mitattu_osoitin_vektorin_pituus)

print("Koordinaatit (x, y):", koordinaatit)
