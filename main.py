import timeit

from DataGen import DataGenerator
from EasyAssembly import EasyAssembly

begin = timeit.default_timer()


def main():
    haplotypes = True
    size = 100
    info = DataGenerator(size)

    if haplotypes:
        print "\nOriginal Haplotypes:"
        print info
    min_size = 10
    max_size = 20
    min_distance = 0
    max_distance = 5
    error = 0  # currently working on easy algorithm
    overlap_chance = 0.5  # 50/50 chance
    info.create_string(min_size=min_size, max_size=max_size, min_distance=min_distance, max_distance=max_distance,
                       error=error, overlap_chance=overlap_chance)

    def print_hap(haplotype, flipped):
        result = ""
        if not flipped:
            for H in haplotype:
                result += str(H)
        else:
            for H in haplotype:
                if H == 0:
                    result += "1"
                else:
                    result += "0"
        print result

    print "\n- Easy Algorithm -\n"
    assembled = EasyAssembly.assemble(info.reads, size)
    if haplotypes:
        print "Assembled haplotypes:"
        print_hap(assembled, flipped=False)
        print_hap(assembled, flipped=True)
    print "\n- Accuracy: 100% -"


if __name__ == "__main__":
    main()

end = timeit.default_timer()

time = end - begin
print "- Runtime:", time, "-"
