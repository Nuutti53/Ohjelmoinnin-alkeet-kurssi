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
    print(f"Ruudusta {sarake_nr, rivi_nr} löytyy {ELAIMET[ruudussa_oleva_merkki]}")

def tutki_kentta(kentta):
    """
    Funktio tutkii kentän sisällön käymällä sen kokonaan läpi kutsuen tutki_ruutu-funktiota
    jokaiselle kentän sisällä olevalle alkiolle.
    """    
    for rivi_index, rivi in enumerate(kentta):
        for ruutu_index, ruutu in enumerate(rivi):
            try:
                tutki_ruutu(ruutu, rivi_index, ruutu_index)
            except KeyError:
                pass

pelto = [
    [" ", "a", " ", " ", "l"],
    [" ", "k", "@", "k", " "],
    ["h", " ", "a", "k", " "]
]

tutki_kentta(pelto)
