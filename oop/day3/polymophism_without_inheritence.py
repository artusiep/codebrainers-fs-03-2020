class Dzwi:
    def open(self):
        print(f"Open {self} of id: {id(self)}")

    def __str__(self):
        return "SOME RANDOM STING"


class Butelka:
    def open(self):
        print(f"Open {self} of id: {id(self)}")

    def __str__(self):
        return "Jestem Butelką"


class Okno:
    def open(self):
        print(f"Open {self} of id: {id(self)}")


class Plik:
    def open(self):
        print(f"Open {self} of id: {id(self)}")


drzwi = Dzwi()
drzwi_str = str(drzwi)
things = [drzwi, Butelka(), Okno(), Plik()]
for thing in things:
    thing.open()

print(id(drzwi))

# Duck Typing
