from files import files
from graph import Graph, karger_stein
from file_parser import parse_file
import numpy as np
np.set_printoptions(linewidth=130)

afile = files[2]
print("parsing ", afile)
g = parse_file("dataset/{}".format(afile))
k = int(np.floor(g.n_vertices / np.sqrt(2)) + 1)
amin = karger_stein(g)
print(amin)
