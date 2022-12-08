class Fabric:
    def __init__(self, countryOfOrigin, color):
        self.countryOfOrigin = countryOfOrigin
        self.color = color

    def __str__(self):
        return self.countryOfOrigin + "("+ str(self.color) +")"

tt1 = Fabric("Canada", "cream")

print(tt1)
