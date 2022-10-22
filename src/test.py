from time import perf_counter_ns
from file_parser import parse_file
import gc
from multiprocessing import Pool, cpu_count
from rapresentation import write_to_csv
from karger_stein import karger_stein
from stoer_wagner import stoer_wagner
from hybrid import hybrid

def test_sw(fname):
    print("(sw) working on {}".format(fname))
    graph = parse_file("dataset/{}".format(fname))
    gc.disable()
    start_time = perf_counter_ns()
    amin, d_time = stoer_wagner(graph)
    end_time = perf_counter_ns()
    gc.enable()

    run_time = end_time - start_time
    disc_time = d_time - start_time
    n, m = graph.n_vertices, graph.n_edges

    run = (fname, run_time, disc_time, n, m, amin)
    write_to_csv(run, "stoer_wagner")

    return run

def test_ks(fname):
    print("(ks) working on {}".format(fname))
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

def test_hy(fname):
    print("(hy) working on {}".format(fname))
    graph = parse_file("dataset/{}".format(fname))
    gc.disable()
    start_time = perf_counter_ns()
    amin, d_time = hybrid(graph)
    end_time = perf_counter_ns()
    gc.enable()

    run_time = end_time - start_time
    disc_time = d_time - start_time
    n, m = graph.n_vertices, graph.n_edges

    run = (fname, run_time, disc_time, n, m, amin)
    write_to_csv(run, "hybrid")

    return run
# Run the alg on the number of instances
def measure_run_time(test_f, inputs, num_instances=(cpu_count() - 2)):
    with Pool(num_instances) as p:
        return p.map(test_f, inputs, chunksize=num_instances)
