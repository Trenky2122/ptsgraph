from graph import Graph

#I do not use unittesting framework on purpose here to show that you can do quite a lot without it

g1 = Graph()
assert(g1.previous is None)

assert(g1.hasvertex(1) is False)
g2 = g1.addvertex(1)
assert(g2.hasvertex(1) is True)
assert(g1.hasvertex(1) is False)
assert(g2.hasvertex(2) is False)

g3 = g2.addvertex(2)
g4 = g3.addvertex(3)
assert(g4.hasedge(1,2) is False)
assert(g4.hasedge(2,1) is False)
g5 = g4.addedge(2,3)
assert(g5.hasedge(1,2) is False)
assert(g5.hasedge(2,1) is False)
assert(g5.hasedge(3,2) is True)
assert(g5.hasedge(2,3) is True)
assert(g4.hasedge(3,2) is False)
assert(g4.hasedge(2,3) is False)

print("Tests complete.")