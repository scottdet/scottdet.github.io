import random


from Read import Read


# generate some random strings consisting of 1's and 0's
class DataGenerator(object):
    def __init__(self, size):
        self.size = size
        self.H1 = []
        self.H2 = []
        self.reads = []
        for i in range(0, size / 20):
            before = random.getrandbits(20)    # get 25 random integers
            for j in range(0, 20):
                after = (before & (1 << j)) >> j    # change integer values to 0's and 1's
                self.H1.append(after)
                self.H2.append(~after & 1)  # H2 is complimentary to H1

    def create_string(self, min_size, max_size, min_distance, max_distance, error, overlap_chance):
        index = 0
        while index < self.size:
            read_size = random.randint(min_size, max_size)
            if random.random() < 0.5:
                data = self.H1[index:index + read_size]
            else:
                data = self.H2[index:index + read_size]
            if len(data) > 0:
                read = Read(index, data, error)     # error will be 0 for now
                self.reads.append(read)
            if random.random() > overlap_chance:
                index += min(random.randint(min_distance, max_distance), read_size - 1)

    # make it so we can read what the original haplotype looked like not just 0x00... computer stuff
    def __repr__(self):
        result = ""
        for H in self.H1:
            result += str(H)
        result += "\n"
        for H in self.H2:
            result += str(H)
        return result
