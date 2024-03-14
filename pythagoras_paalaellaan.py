def laske_sivun_pituus(hypotenuusa):
    sivun_pituus = (hypotenuusa / (2 ** (1/2)))
    return sivun_pituus

mitattu_hypotenuusa = float(input("Anna tasakylkisen kolmion hypotenuusan pituus: "))
kylkien_pituus = laske_sivun_pituus(mitattu_hypotenuusa)
print("Kylkien pituus:", round(kylkien_pituus, 4))
