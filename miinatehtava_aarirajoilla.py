#sanakirja
TULOSTUKSET = {
    "ulkona": "Antamasi ruutu on kentän ulkopuolella.",
    "nurkassa": "Antamasi ruutu on kentän nurkassa.",
    "laidalla": "Antamasi ruutu on kentän laidalla.",
    "keskellä": "Antamasi ruutu on keskikentällä."
}

#Funktiot
def sijainti_kentalla(x_koord, y_koord, kentta_leveys, kentta_korkeus):
    if x_koord == 0 and y_koord == 0: 
        return "nurkassa"
    if x_koord == kentta_leveys - 1 and y_koord == kentta_korkeus - 1: 
        return "nurkassa"
    if x_koord == 0 and y_koord == kentta_korkeus - 1: 
        return "nurkassa"
    if y_koord == 0 and x_koord == kentta_leveys - 1: 
        return "nurkassa"
    if x_koord == 0 and y_koord > 0: 
        return "laidalla"
    if y_koord == 0 and x_koord > 0: 
        return "laidalla"
    if x_koord == kentta_leveys - 1 and y_koord > 0: 
        return "laidalla"
    if y_koord == kentta_korkeus - 1 and x_koord > 0: 
        return "laidalla"
    if x_koord >= kentta_leveys or y_koord >= kentta_korkeus: 
        return "ulkona"
    if x_koord < 0 or y_koord < 0: 
        return "ulkona"
    else: 
        return "keskellä"

def tulosta_sijainti(sijainti):
    print(TULOSTUKSET[sijainti])

#Pääohjelma
try:
    annettu_kentan_leveys = int(input("Anna kentän leveys: "))
    annettu_kentan_korkeus = int(input("Anna kentän korkeus: "))
except ValueError:
    print("Anna kokonaisluku")
else:
    if annettu_kentan_korkeus <= 0 or annettu_kentan_leveys <= 0:
        print("Noin pienelle kentälle ei mahdu ainuttakaan ruutua!")
    else:
        try:
            annettu_x_koord = int(input("Anna x-koordinaatti: "))
            annettu_y_koord = int(input("Anna y-koordinaatti: "))
        except ValueError:
            print("Anna kokonaisluku")
        else:
            sijainti_kentalla = sijainti_kentalla(annettu_x_koord, annettu_y_koord, 
                                                  annettu_kentan_leveys, annettu_kentan_korkeus)
            tulosta_sijainti(sijainti_kentalla)