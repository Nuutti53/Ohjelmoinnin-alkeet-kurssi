def valitse_lukumaara(tavara):
    return tavara[1]

tavara = ("a451", 12)
print(valitse_lukumaara(tavara))

inventaario = [("aasi", 12), ("muumimuki", 1), ("varsikirves", 4)]
inventaario.sort(key=valitse_lukumaara, reverse = True)
print(inventaario)
