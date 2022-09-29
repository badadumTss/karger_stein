from time import perf_counter_ns
from tqdm import tqdm
import random
from file_parser import parse_file
from graph import karger_stein
import gc


def measure_run_time(input_name, num_calls, num_instances):
    sum_times = 0.0
    graph = parse_file("dataset/{}".format(input_name))
    amin = 0
    for i in range(num_instances):
        gc.disable()
        start_time = perf_counter_ns()
        for i in range(num_calls):
            amin = karger_stein(graph)
        end_time = perf_counter_ns()
        gc.enable()
        sum_times += (end_time - start_time)/num_calls
    tqdm.write('done.\n')
    avg_time = int(round(sum_times/num_instances))
    # return average time in nanoseconds
    return avg_time, amin, graph.n_vertices, graph.n_edges
