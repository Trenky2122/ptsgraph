from pyrsistent import pmap, pset, thaw

#you may want to use PClass, but we want to learn something
class Graph:
    def __init__(self):
        self._incidence = pmap() #map<int,set<int>>
        
    def _newgraph(self, incidence):
        a = Graph()
        a._incidence = incidence
        return a
            
    def hasvertex(self, v):
        return v in self._incidence
        
    def addvertex(self, v):
        if v in self._incidence:
            return self
        else:
            return self._newgraph(self._incidence.set(v, pset()))
            
    def hasedge(self, v1, v2):
        return v2 in self._incidence[v1]
            
    def addedge(self, v1, v2):
        addv1 = lambda x: x.add(v1)
        addv2 = lambda x: x.add(v2)
        newinc = self._incidence.transform([v1], addv2, [v2], addv1)
        return self._newgraph(newinc)
        
    def neighbours(self, v):
        for el in self._incidence[v]:
            yield el
            
    def removeedge(self, v1, v2):
        removev1 = lambda x: x.remove(v1)
        removev2 = lambda x: x.remove(v2)
        newinc = self._incidence.transform([v1], removev2, [v2], removev1)
        return self._newgraph(newinc)
        
    def removevertex(self, v):
        evo = self._incidence.evolver()
        for v2 in self._incidence[v]:
            evo[v2] = evo[v2].remove(v)
        evo.remove(v)
        return self._newgraph(evo.persistent())
        
        
        