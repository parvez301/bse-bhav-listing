class BSEObject(object):
    def __init__(self, code, name, open, low, close, high):
        self.code = code
        self.name = name
        self.open = open
        self.low = low
        self.close = close
        self.high = high

    def __repr__(self):
        return repr((self.code, self.name, self.open, self.low, self.close, self.high))

    def __cmp__(self, other):
        if hasattr(other, 'close'):
            return self.close.__cmp__(other.close)