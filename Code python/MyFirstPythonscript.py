import pprint

stuff = [carotte, poireau, oeufs, bananes]
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)


