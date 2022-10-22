from rapresentation import *

ks_run = read_csv("karger_stein")
plot(ks_run, 'Karger and Stein', ks_complex)

sw_run = read_csv("stoer_wagner")
plot3D(sw_run, 'Stoer and Wagner', sw_complex)

hy_run = read_csv("hybrid")
plot3D(hy_run, 'Hybrid', hy_complex)
