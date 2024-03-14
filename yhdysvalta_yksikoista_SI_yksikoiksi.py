PITUUSKERTOIMET = {
    "in": 0.0254,
    "\"": 0.0254,
    "ft": 0.3048,
    "'": 0.3048,
    "yd": 0.9144,
    "mi": 1609.344
}

MASSAKERTOIMET = {
    "oz": 28.349523125,
    "lb": 0.45359237
}

TILAVUUSKERTOIMET = {
    "cp": 2.365882365,
    "pt": 4.73176473,
    "qt": 0.946352946,
    "gal": 3.785411784
}

def kysy_arvo():
    while True:
        try:
            luku = float(input("Anna muutettava arvo: "))
        except ValueError:
            print("Arvon tulee olla pelkkä luku")
        else:
            break
    return luku

def kysy_muutettava():
    while True:
        try:
            muutettava = input("Anna muutettava arvo ja yksikkö: ").split("")
            arvo = float(muutettava[0])
            yksikko = muutettava[1]
        except ValueError:
            print("Arvon tulee olla pelkkä luku")
        except IndexError:
            print("Syötteessä tulee olla arvo ja yksikkö välilyönnillä toisistaan erotettuna")
        else:
            return arvo, yksikko

def muunna_metreiksi(mittaus):
    arvo = mittaus["arvo"]
    yksikko = mittaus["yksikko"]
    try:
        metrit = arvo * PITUUSKERTOIMET[yksikko]
    except KeyError:
        mittaus["virheellinen"] = True
    else:
        mittaus["yksikko"] = "m"
        mittaus["arvo"] = metrit

def pituus():
    print("Valitse pituusyksikkö seuraavien joukosta syöttämällä suluissa annettu lyhenne")
    print("Tuuma (in tai \")")
    print("Jalka (ft tai ')")
    print("Jaardi (yd)")
    print("Maili (mi)")
    print()
    while True:
        yksikko = input("Anna muutettava yksikkö: ")
        if not yksikko:
            break
        arvo = kysy_arvo()
        try:
            kerroin = PITUUSKERTOIMET[yksikko]
        except KeyError:
            print("Valitsemaasi yksikköä ei voida muuntaa")
        else:
            print(f"{arvo:.3f} {yksikko} on {arvo * kerroin:.3f} m")

def massa():
    print("Valitse painoyksikkö seuraavien joukosta syöttämällä suluissa annettu lyhenne")
    print("Unssi (oz)")
    print("Pauna (lb)")
    print()
    while True:
        yksikko = input("Anna muutettava yksikkö: ")
        if not yksikko:
            break
        arvo = kysy_arvo()
        try:
            kerroin = MASSAKERTOIMET[yksikko]
        except KeyError:
            print("Valitsemaasi yksikköä ei voida muuntaa")
        else:
            print(f"{arvo:.3f} {yksikko} on {arvo * kerroin:.3f} m")

def tilavuus():
    print("Valitse nestetilavuusyksikkö seuraavien joukosta syöttämällä suluissa annettu lyhenne")
    print("Kupillinen (cp)")
    print("Pintti (pt)")
    print("Varttigallona (qt)")
    print("Gallona (gal)")
    print()
    while True:
        yksikko = input("Anna muutettava yksikkö: ")
        if not yksikko:
            break
        arvo = kysy_arvo()
        try:
            kerroin = TILAVUUSKERTOIMET[yksikko]
        except KeyError:
            print("Valitsemaasi yksikköä ei voida muuntaa")
        else:
            print(f"{arvo:.3f} {yksikko} on {arvo * kerroin:.3f} m")

def lampotila():
    print("Lämpötilamuunnos Fahrenheit-asteista Celsius-asteiksi")
    fahrenheit = kysy_arvo()
    celsius = (5 / 9) * (fahrenheit - 32)
    print(f"{fahrenheit:.2f} °F on {celsius:.2f} °C")


print("Tämä ohjelma muuntaa yhdysvaltalaisia yksiköitä SI-yksiköiksi")
print("Mahdolliset toiminnot:")
print("(P)ituus")
print("(M)assa")
print("(T)ilavuus")
print("(L)ämpotila")
print("(Q)uittaa")
print()
while True:
    valinta = input("Tee valintasi: ").strip().lower()
    if valinta == "p" or valinta == "pituus":
        pituus()
    elif valinta == "m" or valinta == "massa":
        massa()
    elif valinta == "t" or valinta == "tilavuus":
        tilavuus()
    elif valinta == "l" or valinta == "lämpötila":
        lampotila()
    elif valinta == "q" or valinta == "quittaa":
        break
    else:
        print("Valitsemaasi toimintoa ei ole olemassa")
