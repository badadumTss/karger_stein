import matplotlib.pyplot as plt
from rapresentation import read_csv, plot, ks_complex

hy = read_csv("karger_stein")
plot(hy, 'Karger and Stein', ks_complex)

