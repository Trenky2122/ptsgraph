from graph import Graph

#I do not use unittesting framework on purpose here to show that you can do quite a lot without it

g1 = Graph()
assert(g1.previous is None)

assert(g1.hasvertex(1) is False)
g2 = g1.addvertex(1)
assert(g2.hasvertex(1) is True)
assert(g1.hasvertex(1) is False)
assert(g2.hasvertex(2) is False)


print("Tests complete.")