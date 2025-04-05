class Pizza:
    def __init__(self, naam, grootte, topping):
        self.naam = naam
        self.grootte = grootte
        self.topping = topping

    def quel_pizza(self):
        print(f"Een {self.naam} die {self.grootte} groot is, de ingrediënten zijn:")
        for topping in self.topping:
            print(topping)

    def bereken_prijs(self):
        basisprijs = 0.0
        if self.grootte == "25cm":
            basisprijs = 8.99
        elif self.grootte == "30cm":
            basisprijs = 12.99
        elif self.grootte == "3km":
            basisprijs = 8499.99
        basisprijs += len(self.topping) * 1.5
        return basisprijs

margarita = Pizza("margarita", "25cm",["kaas", "tomatensaus"])
margarita.quel_pizza()
print(f"prijs: €{margarita.bereken_prijs():.2f}")
pizza_salami = Pizza("pizza salami", "30cm",["kaas", "tomatensaus", "salami"])
pizza_salami.quel_pizza()
print(f"prijs: €{pizza_salami.bereken_prijs():.2f}")
pizza_hawaii = Pizza("pizza hawaii", "3km",["kaas", "tomatensaus", "ananas"])
pizza_hawaii.quel_pizza()
print(f"prijs: €{pizza_hawaii.bereken_prijs():.2f}")

#print("Welke pizza?")
#naam_PIZZA = input("")
#eigen_pizza = Pizza(naam_PIZZA, "52", '')
#eigen_pizza.quel_pizza()

