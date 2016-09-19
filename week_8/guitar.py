class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        guitar_age = 2016 - self.year
        return guitar_age

    def is_vintage(self):
        guitar_age = self.get_age()
        if guitar_age >= 50:
            return "(Vintage)"
        else:
            return ""
