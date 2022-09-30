from files import files
from graph import Graph, karger_stein
from file_parser import parse_file
from tqdm import tqdm
from test import measure_run_time
from representation import plot, print_table, write_to_csv
import matplotlib.pyplot as plt
import datetime
import csv
import numpy as np

# misura il runtime
num_calls = 10
num_instances = 3
run_times_karger = [(afile, ) + measure_run_time(karger_stein, afile, num_calls, num_instances)
                    for afile in tqdm(files)]

write_to_csv(run_times)
print_table(run_times)
plot(run_times)
