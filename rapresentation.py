import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Result rapresentation

# All the functions defined here want the data as a list of tuples in
# the form
# `(name, time, discovery time, #vertices, #edges, solution)`


def print_table(data):
    fstr = "{:<25}{:<12}{:<12}{:<15}{:<15}{:<13}"
    print(fstr.format("name", "time", "d_time", "n_vertices", "n_edges", "sol"))
    print("-"*80)
    for (afile, time, d_time, sol, n, m) in data:
        print(fstr.format(afile, time, d_time, n, m, sol))


def write_to_csv(data):
    with open("karger_stein_results.txt", 'w') as f:
        writer = csv.writer(f)
        for el in data:
            writer.writerow(el)


def read_csv(file_name):
    to_ret = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            to_ret += (tuple(row),)
    return to_ret


def ks_complex(n,m):
    return (n**2)*(np.log(n) ** 3)

def sw_complex(n,m):
    return (m*n) + (n**2)*(np.log(n))

def plot(data, alg_name, f):
    print("Plotting ...")
    times = [time for (afile, time, d_time, sol, n, m) in data]
    n = [n for (afile, time, d_time, sol, n, m) in data]
    m = [m for (afile, time, d_time, sol, n, m) in data]

    # calc coefficent in order to see a better function
    c = times[0] / f(n[0], m[0])

    # plot against n^2(log n)^3
    x = range(max(times))
    z = [c*f(n,m) for n,m in zip(n,m)]

    ax = plt.axes(projection='3d')
    ax.scatter(n, times, label="{} runs".format(alg_name))

    ax.plot(n, m, z, 'y', label='complexity function')
    ax.legend()
    plt.ylabel("time (ns)")
    plt.xlabel("input nodes")
    name = 'plot_{}.eps'.format(datetime.datetime.now())
    plt.savefig(name, format='eps')
    print("Saved plot to {}".format(name))
