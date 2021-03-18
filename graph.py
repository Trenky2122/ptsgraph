from pyrsistent import pmap, pset, thaw
from labeledint import labeledint

#you may want to use PClass, but we want to learn something
class Graph:
    def __init__(self):
        self._incidence = pmap() #map<labeledint,set<labeledint>>
        
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
            return self._newgraph(self._incidence.set(labeledint(v, None), pset()))
            
    def hasedge(self, v1, v2):
        return v2 in self._incidence[v1]
        
    def neighbours(self, v):
        for el in self._incidence[v]:
            yield el

    def _dostuffwithedge(self, v1, v2, fun):
        modifyv1 = fun(v1)
        modifyv2 = fun(v2)
        newinc = self._incidence.transform([v1], modifyv2, [v2], modifyv1)
        return self._newgraph(newinc)
            
    def addedge(self, v1, v2):
        return self._dostuffwithedge(labeledint(v1, None), labeledint(v2, None), lambda v: (lambda x: x.add(labeledint(v, None))))
                    
    def removeedge(self, v1, v2):
        return self._dostuffwithedge(v1, v2, lambda v: (lambda x: x.remove(v)))
        
    def removevertex(self, v):
        evo = self._incidence.evolver()
        for v2 in self._incidence[v]:
            evo[v2] = evo[v2].remove(v)
        evo.remove(v)
        return self._newgraph(evo.persistent())

    def labelvertex(self, v, label):
        if v in self._incidence:
            newinc = self._incidence.remove(v)
            newinc = newinc.set(labeledint(v, label), pset())
            return self._newgraph(newinc)
        else:
            newg = self.addvertex(v)
            return newg.labelvertex(v, label)

    def getlabelvertex(self, v):
        for vt in self._incidence:
            if vt == v:
                return vt.label

    def labeledge(self, v1, v2, label):
        tmpg = self._newgraph(self._incidence)
        if self.hasedge(v1, v2):
            tmpg = self.removeedge(v1, v2)
        return self._dostuffwithedge(v1, v2, lambda v: (lambda x: x.add(labeledint(v, label))))

    def getlabeledge(self, v1, v2):
        neighbours = self._incidence[v1]
        for vt in neighbours:
            if vt == v2:
                return vt.label

    def transformvertices(self, vertices, transformation):
        newinc = self._incidence.copy()
        for v in self._incidence:
            if v in vertices:
                edges = self._incidence[v].copy()
                newinc = newinc.remove(v)
                newv = transformation(v)
                newinc = newinc.set(newv, edges)
        return self._newgraph(newinc)

    def transformedge(self, v1, v2, transformation):
        return self._dostuffwithedge(v1, v2, transformation)