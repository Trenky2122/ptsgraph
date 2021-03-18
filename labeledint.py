class labeledint(int):
    def __new__(cls, value, label, *args, **kwargs):
        return super(cls, cls).__new__(cls, value)

    def __init__(self, value, label):
        self.__label = label
        int.__init__(self)
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