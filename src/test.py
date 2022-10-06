from time import perf_counter_ns
from tqdm import tqdm
from file_parser import parse_file
import gc
import copy
from multiprocessing import Pool, cpu_count
from rapresentation import write_to_csv


def measure_run_time(func, input_name, alg_name,
                     num_instances=(cpu_count() - 2)):
    tqdm.write('running on {} with {} instances\n'.format(input_name, num_instances))
    graph = parse_file("dataset/{}".format(input_name))
    glist = [copy.deepcopy(graph) for i in range(num_instances)]

    with Pool(num_instances) as p:
        gc.disable()
        start_time = perf_counter_ns()
        # Run the alg on the number of instances
        rlist = p.map(func, glist) # [(min, d_time)]
        end_time = perf_counter_ns()
        gc.enable()
        max_time = int(round((end_time - start_time)))
        avg_disc = int(sum([(d_time - start_time) for amin, d_time in rlist]) / (num_instances))
        amin = min([amin for amin, d_time in rlist])
        tqdm.write('done.\n')

        run = max_time, avg_disc, amin, graph.n_vertices, graph.n_edges

        # Write partial run data to file
        write_to_csv(run, alg_name)
        return run
