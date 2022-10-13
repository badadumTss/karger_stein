from time import perf_counter_ns
from tqdm import tqdm
from file_parser import parse_file
import gc
import copy
from multiprocessing import Pool, cpu_count
from rapresentation import write_to_csv
import numpy as np
from karger_stein import karger_stein
from stoer_wagner import stoer_wagner

def divide_chunks(l, n):     
    for i in range(0, len(l), n):
        yield l[i:i + n]

def test_sw(fname):
    tqdm.write("(sw) working on {}".format(fname))
    graph = parse_file("dataset/{}".format(fname))
    gc.disable()
    start_time = perf_counter_ns()
    cut, d_time = stoer_wagner(graph)
    end_time = perf_counter_ns()
    gc.enable()
    
    run_time = end_time - start_time
    disc_time = d_time - start_time
    amin = graph.cut_weight(cut)
    n, m = graph.n_vertices, graph.n_edges

    run = (fname, run_time, disc_time, n, m, amin)
    write_to_csv(run, "stoer_wagner")

    return run

def test_ks(fname):
    tqdm.write("(ks) working on {}".format(fname))
    graph = parse_file("dataset/{}".format(fname))
    gc.disable()
    start_time = perf_counter_ns()
    amin, d_time = karger_stein(graph)
    end_time = perf_counter_ns()
    gc.enable()
    
    run_time = end_time - start_time
    disc_time = d_time - start_time
    n, m = graph.n_vertices, graph.n_edges

    run = (fname, run_time, disc_time, n, m, amin)
    write_to_csv(run, "karger_stein")

    return run

# Run the alg on the number of instances
def measure_run_time(test_f, inputs, num_instances=(cpu_count() - 2)):
    with Pool(num_instances) as p:
        return p.map(test_f, inputs, chunksize=num_instances)
