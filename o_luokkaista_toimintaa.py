def laske_ninjat(x_koord, y_koord, huone):
    """
    Laskee annetussa huoneessa yhden ruudun ympärillä olevat ninjat ja palauttaa
    niiden lukumäärän. Funktio toimii sillä oletuksella, että valitussa ruudussa ei
    ole ninjaa - jos on, sekin lasketaan mukaan.
    """

    ninjat = 0
    for i in range(max(0, y_koord-1), min(len(huone), y_koord+2)):
        for j in range(max(0, x_koord-1), min(len(huone[0]), x_koord+2)):
            if huone[i][j] == 'N':
                ninjat += 1
    return ninjat

# Esimerkki huoneesta
huone = [
    ['N', ' ', ' ', ' ', ' '],
    ['N', 'N', 'N', 'N', ' '],
    ['N', ' ', 'N', ' ', ' '],
    ['N', 'N', 'N', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

print(" ", "- " * 5)
for rivi in huone:
    print("|", " ".join(rivi), "|")
print(" ", "- " * 5)

kysytty_x = int(input("Anna x: "))  # Ruudun x-koordinaatti
kysytty_y = int(input("Anna y: "))  # Ruudun y-koordinaatti
print("Ympärillä olevat ninjat:", laske_ninjat(kysytty_x, kysytty_y, huone))
