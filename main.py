from files import files
from graph import Graph, karger_stein
from file_parser import parse_file
import numpy as np
from tqdm import tqdm
from test import measure_run_time
np.set_printoptions(linewidth=130)

num_calls = 10
num_instances = 3
run_times = [measure_run_time(afile, num_calls, num_instances) + (afile,) for afile in tqdm(files)]

print("{:<8}\t{:<12}{:<13}".format("Name", "Time", "Solution"))
print("-"*80)
for (time, sol, afile) in run_times:
    print("{}\t{:<12}{:<13}".format(afile, time, sol))
