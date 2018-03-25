import convert
import random


def gen_string( base, length ):
    s = ''
    for x in range(length):
        s += str(random.randint(0,base))
    return s

import matplotlib.pyplot as plt

# Say I have a thing with N states.
# A unary function has N^N states.
# N 'digits' with N possible values each.
if __name__ == '__main__':

    base = 2
    for r in [convert.n2s(n,base,base) for n in range(base**base)]:
        graphs = [[] for k in range(base)]
        for x in range(base):
            for compose in range(base):
                graphs[compose].append(x)
                #print(compose, ":", x, r, r[x])
                x = int(r[x])

        for g in graphs:
            plt.plot(g)
        plt.show()


