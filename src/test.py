from time import perf_counter_ns
from tqdm import tqdm
from file_parser import parse_file
import gc
import copy
from multiprocessing import Pool, cpu_count
from rapresentation import write_to_csv
import numpy as np

def divide_chunks(l, n):     
    for i in range(0, len(l), n):
        yield l[i:i + n]

# Run the alg on the number of instances
def measure_run_time(func, inputs, alg_name,
                     num_instances=(cpu_count() - 2)):

    graphs = [parse_file("dataset/{}".format(name)) for name in inputs]

    with Pool(num_instances) as p:
        runs = []
        tot = int(np.ceil(len(inputs)/num_instances))
        
        for i, chunk in enumerate(tqdm(divide_chunks(graphs, num_instances), total=tot)):
            
            gc.disable()
            start_time = perf_counter_ns()
            tqdm.write("Working on")
            for el in chunk:
                tqdm.write("{}".format(el))
            res = p.map(func, chunk) # [(min, n, m, d_time, end_time)]
            gc.enable()
        
            for j, (amin, n, m, d_time, end_time) in enumerate(res):
                run_time = int(round((end_time - start_time)))
                d_time = d_time - start_time
                run = inputs[i*num_instances + j], run_time, d_time, amin, n, m
                # Write partial run data to file
                write_to_csv(run, alg_name)
                runs += [run]

            decor = '='*20
            tqdm.write("{} Chunk {} done {}".format(decor, i, decor))

        return runs
