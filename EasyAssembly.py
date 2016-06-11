class EasyAssembly:

    @classmethod
    def assemble(cls, reads, size):
        hap = [0] * size
        hap_index = 0
        read_index = 0
        while hap_index < size:
            while read_index < len(reads) - 1 and reads[read_index + 1].start < hap_index:
                read_index += 1
            read = reads[read_index]

            if hap_index > 0 and read.data[0] != hap[read.start]:
                hap[hap_index:read.start + read.size] = list(read.flipped[hap_index - read.start:])
            else:
                hap[hap_index:read.start + read.size] = list(read.data[hap_index - read.start:])

            hap_index += read.size - (hap_index - read.start)

        return hap
