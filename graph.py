from pyrsistent import pmap, pset

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
            