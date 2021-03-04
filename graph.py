from pyrsistent import pmap, pset, thaw

#you may want to use PClass, but we want to learn something
class Graph:
    def __init__(self):
        self._incidence = pmap() #map<int,set<int>>
        self._previous = None
        
    def _newgraph(self, incidence):
        a = Graph()
        a._incidence = incidence
        a._previous = self
        return a
    
    @property
    def previous(self):
        return self._previous
        
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
        evo = self._incidence.evolver()
        evo[v1] = evo[v1].add(v2)
        evo[v2] = evo[v2].add(v1)
        return self._newgraph(evo.persistent())
        
    def neighbours(self, v):
        for el in self._incidence[v]:
            yield el
            
    def removeedge(self, v1, v2):
        evo = self._incidence.evolver()
        evo[v1] = evo[v1].remove(v2)
        evo[v2] = evo[v2].remove(v1)
        return self._newgraph(evo.persistent())
        
        