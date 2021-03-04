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

assert(set(g5.neighbours(1)) == set())
assert(set(g5.neighbours(2)) == set({3}))
assert(set(g5.neighbours(3)) == set({2}))

g6 = g5.addedge(3,2)
assert(set(g6.neighbours(1)) == set())
assert(set(g6.neighbours(2)) == set({3}))
assert(set(g6.neighbours(3)) == set({2}))

g7 = g6.addedge(2,1)
assert(set(g7.neighbours(1)) == set({2}))
assert(set(g7.neighbours(2)) == set({1,3}))
assert(set(g7.neighbours(3)) == set({2}))

g8 = g7.removeedge(3,2)
assert(set(g8.neighbours(1)) == set({2}))
assert(set(g8.neighbours(2)) == set({1}))
assert(set(g8.neighbours(3)) == set())

g9 = g7.removevertex(2)
assert(g9.hasvertex(1) is True)
assert(g9.hasvertex(2) is False)
assert(set(g9.neighbours(1)) == set())
assert(set(g9.neighbours(3)) == set())

g10 = g7.removevertex(1)
assert(g10.hasvertex(1) is False)
assert(g10.hasvertex(2) is True)
assert(set(g10.neighbours(2)) == set({3}))
assert(set(g10.neighbours(3)) == set({2}))

print("Tests complete.")