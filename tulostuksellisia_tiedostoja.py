def nayta_tulokset(tiedosto):
    with open(tiedosto, "r") as kohde:
        for data in kohde:
            pelaaja1, pelaaja2, piste1, piste2 = data.split(",")
            print(f"{pelaaja1} {piste1} - {piste2.strip()} {pelaaja2}")

nayta_tulokset("hemulicup.csv")
