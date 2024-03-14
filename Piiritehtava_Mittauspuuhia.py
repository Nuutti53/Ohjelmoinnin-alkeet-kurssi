import cmath

def laske_osoitinmuoto(komponentin_tyyppi, komponentin_arvo, jännitelähteen_taajuus = 0):
    if komponentin_tyyppi == "r":
        print("Vastus: impedanssi = R")
        osoittimen_pituus = komponentin_arvo
        osoittimen_kulma_radiaaneina = cmath.polar(osoittimen_pituus)
    elif komponentin_tyyppi == "l":
        print("Kela: impedanssi = 2*cmath.pi * f * L * 1j")
        osoittimen_pituus = float(2 * cmath.pi * jännitelähteen_taajuus * komponentin_arvo * 1j)
        osoittimen_kulma_radiaaneina = cmath.polar(osoittimen_pituus)
    elif komponentin_tyyppi == "c":
        print("Kondensaattori: impedanssi = 1 / (2*cmath.pi * f * C * 1j)")
        osoittimen_pituus = float(1 / (2 * cmath.pi * jännitelähteen_taajuus * komponentin_arvo * 1j))
        osoittimen_kulma_radiaaneina = cmath.polar(osoittimen_pituus)
        
    return osoittimen_pituus, osoittimen_kulma_radiaaneina

kysytty_komponentin_tyyppi = input("Anna komponentin tyyppi (R, L, C): ").lower()
kysytty_komponentin_arvo = float(input("Anna komponentin arvo: "))
kysytty_jännitelähteen_taajuus = float(input("Anna komponentin taajuus: "))
palautus = laske_osoitinmuoto(kysytty_komponentin_tyyppi, kysytty_komponentin_arvo, kysytty_jännitelähteen_taajuus)
print(f"Komponentin impedanssi osoitinmuodossa: {palautus:0.3f}")