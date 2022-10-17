import matplotlib.pyplot as plt
from rapresentation import read_csv, plot3D, hy_complex

hy = read_csv("hybrid")
plot3D(hy, 'Hybrid', hy_complex)

