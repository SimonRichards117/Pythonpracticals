from Week_8.guitar import Guitar

# guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.4)
# guitar2 = Guitar("Gibson L-5 CES", 2011, 16035.4)
#
# print(guitar1,guitar1.get_age(),guitar1.is_vintage())
# print(guitar2,guitar2.get_age(),guitar2.is_vintage())
list_of_guitars = []
guitar_name = input("""My Guitars!
name: """)
while guitar_name != "":
    guitar_year = input("Year: ")
    guitar_cost = input("Cost: $")
    guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    list_of_guitars.append(guitar)
    print(guitar, " Added")
    guitar_name = input("name:")

list_of_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
list_of_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


i = 0
for guitars in list_of_guitars:
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitars.name, guitars.year, guitars.cost,
                                                               guitars.is_vintage()))
    i += 1