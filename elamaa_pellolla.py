ELAIMET = {
    "a": "aasi",
    "k": "koira",
    "@": "kissa",
    "h": "hemuli",
    "l": "lammas"
}

def tutki_ruutu(ruudussa_oleva_merkki, rivi_nr, sarake_nr):
    """
    Funktio tutkii ruudun - jos siellä on eläin, se tulostaa eläimen sijainnin sekä nimen.
    """
    try:
        print(f"Ruudusta {sarake_nr, rivi_nr} löytyy {ELAIMET[ruudussa_oleva_merkki]}")
    except KeyError:
        pass  

def tutki_kentta(kentta):
    """
    Funktio tutkii kentän sisällön käymällä sen kokonaan läpi kutsuen tutki_ruutu-funktiota
    jokaiselle kentän sisällä olevalle alkiolle.
    """    
    for rivi_index, rivi in enumerate(kentta):
        for ruutu_index, ruutu in enumerate(rivi):
            print(rivi_index, rivi, ruutu_index, ruutu)

    

pelto = [
    [" ", "a", " ", " ", "l"],
    [" ", "k", "@", "k", " "],
    ["h", " ", "a", "k", " "]
]

tutki_kentta(pelto)
tutki_ruutu(tutki_kentta(pelto))
