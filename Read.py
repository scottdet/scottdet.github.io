import random


# create readable string
class Read(object):
    def __init__(self, start, data, error):
        self.start = start
        self.data = [H if error == 0 or random.random() > error else random.choice([0, 1]) for H in data]
        self.size = len(self.data)
        self.flipped = [~H & 1 for H in data]

    # repr will return a string containing a printable representation of an object
    def __repr__(self):
        result = ""
        for _ in range(0, self.start):
            result += " "
        for H in self.data:
            result += str(H)
        return result
