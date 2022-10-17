import matplotlib.pyplot as plt
from rapresentation import read_csv, save_plot

hy = read_csv("hybrid")
ks = read_csv("karger_stein")
sw = read_csv("stoer_wagner")

hy = [(n,m,time) for (afile, time, d_time, n, m, sol) in hy]
ks = [(n,m,time) for (afile, time, d_time, n, m, sol) in ks]
sw = [(n,m,time) for (afile, time, d_time, n, m, sol) in sw]

plt.clf()
plt.cla()
plt.close()


ax = plt.axes(projection='3d')
ax.set_xlabel('vertices')
ax.set_ylabel('edges')
ax.set_zlabel('time');

ax.scatter(list(map(lambda x : x[0], hy)),
           list(map(lambda x : x[1], hy)),
           list(map(lambda x : x[2], hy)),
           label="hybrid runs",
           c='y')

ax.scatter(list(map(lambda x : x[0], sw)),
           list(map(lambda x : x[1], sw)),
           list(map(lambda x : x[2], sw)),
           label="Stoer and Wagner runs",
           c='b')

ax.scatter(list(map(lambda x : x[0], ks)),
           list(map(lambda x : x[1], ks)),
           list(map(lambda x : x[2], ks)),
           label="Karger and Stein runs",
           c='r')

ax.legend()
save_plot("Discovery comp")

