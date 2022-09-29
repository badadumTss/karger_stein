from files import files
from graph import Graph, karger_stein
from file_parser import parse_file
import numpy as np
from tqdm import tqdm
from test import measure_run_time
import matplotlib.pyplot as plt
import datetime
import csv

num_calls = 10
num_instances = 3
run_times = [(afile, ) + measure_run_time(afile, num_calls, num_instances)
             for afile in tqdm(files)]

fstr = "{:<25}{:<12}{:<12}{:<15}{:<15}{:<13}"
print(fstr.format("name", "time", "d_time", "n_vertices", "n_edges", "sol"))
print("-"*80)
for (afile, time, d_time, sol, n, m) in run_times:
    print(fstr.format(afile, time, d_time, n, m, sol))

with open("karger_stein_results.txt", 'w') as f:
    writer = csv.writer(f)
    for el in run_times:
        writer.writerow(el)

print("Plotting ...")
times = [time for (afile, time, d_time, sol, n, m) in run_times]
n = [n for (afile, time, d_time, sol, n, m) in run_times]

def O(n):
    return (n**2)*(np.log(n) ** 3)

# calc coefficent in order to see a better function
c = times[0] / O(n[0])

# plot against n^2(log n)^3
x = range(max(n) + 5)
y = [c*O(n) for n in x]

ax = plt.gca()
ax.scatter(n, times, label="karger_stein runs")

ax.plot(list(x), y, 'y', label=r'$n^3\log^3{n}$')
ax.legend()
plt.ylabel("time (ns)")
plt.xlabel("input nodes")
name = 'plot_{}.eps'.format(datetime.datetime.now())
plt.savefig(name, format='eps')
print("Saved plot to {}".format(name))
