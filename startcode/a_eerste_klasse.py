class Dier:
    def __init__(self, naam, geluid):
        self.naam = naam
        self.geluid = geluid

    def maak_geluid(self):
        print(f"De {self.naam} zegt '{self.geluid}'.")


hond = Dier("hond", "woef")
hond.maak_geluid()
kat = Dier("kat", "miauw")
kat.maak_geluid()
koe = Dier("koe", "bêêê")
koe.maak_geluid()