class labeledint(int):
    def __new__(cls, value, label, *args, **kwargs):
        return super(cls, cls).__new__(cls, value)

    def __init__(self, value, label):
        self.__label = label
        int.__init__(self)

    def __add__(self, other):
        res = super(labeledint, self).__add__(other)
        return labeledint(res, self.__label)

    def __sub__(self, other):
        res = super(labeledint, self).__sub__(other)
        return labeledint(res, self.__label)

    def __mul__(self, other):
        res = super(labeledint, self).__mul__(other)
        return labeledint(res, self.__label)

    def __truediv__(self, other):
        res = super(labeledint, self).__truediv__(other)
        return labeledint(res, self.__label)

    def __floordiv__(self, other):
        res = super(labeledint, self).__floordiv__(other)
        return labeledint(res, self.__label)
    @property
    def label(self):
        return self.__label

    def __repr__(self):
        return ("labeledint(%d) " % int(self))+self.labeltostr()

    def __str__(self):
        return self.labeltostr()+": %d" % int(self)

    def labeltostr(self):
        if self.__label is None:
            return '';
        else:
            return str(self.__label)