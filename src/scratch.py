import matplotlib.pyplot as plt
from rapresentation import read_csv, plot, ks_complex

ks = read_csv("karger_stein")
sw = read_csv("stoer_wagner")
hy = read_csv("hybrid")

ks = [(name, sol) for (name, r, d, n, m, sol) in ks]
sw = [(name, sol) for (name, r, d, n, m, sol) in sw]
hy = [(name, sol) for (name, r, d, n, m, sol) in hy]

ks = sorted(ks)
sw = sorted(sw)
hy = sorted(hy)

for i, el in enumerate(zip(ks,sw,hy)):
    if el[0] != el[1] or el[0] != el[1] or el[1] != el[2]:
        print(el)
