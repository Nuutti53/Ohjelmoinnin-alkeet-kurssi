def pyyda_syote(x, y):
    luku = input("Anna kokonaisluku: ")
    return luku

luku = pyyda_syote(
    "Anna kokonaisluku: ",
    "Et antanut kokonaislukua"
)
print(f"Annoit kokonaisluvun {luku}! Nohevaa toimintaa!")
hemulit = pyyda_syote(
    "Montako hemulia mahtuu muumitaloon? ",
    "Tämä ei ollut kelvollinen hemulien lukumäärä!"
)
print(f"Muumitaloon mahtuu {hemulit} hemulia")
