import math

def laske_nelio_ala(sivun_pituus):
    ala = sivun_pituus ** 2
    return ala

def laske_sektorin_ala(sade, sisakulma):
    sektorin_ala = sisakulma/360 * math.pi * sade ** 2 
    return sektorin_ala

def laske_sivun_pituus(hypotenuusa):
    sivun_pituus = (hypotenuusa / (2 ** (1/2)))
    return sivun_pituus

 # kuvion alan laskenta tapahtuu kokonaan
 # tämän funktion sisällä kutsumalla
 # aiempia funktioita välituloksia varten
def laske_kuvion_ala(x):
    nelion_ala = laske_nelio_ala(x)
    kolmion_ala = ((laske_sivun_pituus(x) ** 2) / 2)
    sektorin1_ala = laske_sektorin_ala(laske_sivun_pituus(x), 45)
    ison_nelion_ala = ((laske_sivun_pituus(x) * 2) ** 2)
    sektorin2_ala = laske_sektorin_ala(laske_sivun_pituus(x) * 2, 270)
    
    kuvion_ala = nelion_ala + kolmion_ala + sektorin1_ala + ison_nelion_ala + sektorin2_ala
    
    return kuvion_ala


# pääohjelma joka kysyy x:n arvon
# kutsuu laskufunktiota ja tulostaa alan
# pyöristettynä
mitattu_x = float(input("Anna x: "))
print("Kuvion ala:", round(laske_kuvion_ala(mitattu_x), 4))
