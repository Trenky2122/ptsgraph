from pyrsistent import pmap, pset

#you may want to use PClass, but we want to learn something
class Graph:
    def __init__(self):
        self._incidence = pmap()
        self._previous = None
    
    @property
    def previous(self):
        return self._previous