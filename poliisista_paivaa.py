try:
    kulkema_matka = float(input("Anna auton kulkema matka (m): "))
    kulunut_aika = float(input("Anna matkaan kulunut aika (s): "))
except ValueError:
    print("Vähemmän donitseja, enemmän puhtaita numeroita.")
else:
    nopeus = (kulkema_matka) / (kulunut_aika) * 3.6
    print(f"{kulkema_matka:0.2f} metriä {kulunut_aika:0.2f} " 
          f"sekunnissa kulkeneen auton nopeus on {nopeus:0.2f} km/h")
          