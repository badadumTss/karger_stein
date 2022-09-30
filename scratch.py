from files import files
from graph import Graph, stoer_wagner, karger_stein
from file_parser import parse_file
from tqdm import tqdm
from test import measure_run_time
from rapresentation import plot, print_table, write_to_csv, sw_complex
import matplotlib.pyplot as plt
import datetime
import csv
import numpy as np

# misura il runtime
num_calls = 10
num_instances = 3
decor = '='*10
frange = files[:8]
gen = tqdm(frange)

# Stoer and Wagner
print("{} STOER AND WAGNER {}".format(decor, decor))
run_time = [(afile, ) + measure_run_time(stoer_wagner, afile, num_calls, num_instances) for afile in gen]
print_table(run_time)
plot(run_time, 'stoer and wagner', sw_complex)

# Karger Stein
gen = tqdm(frange)
print("\n{} KARKGER AND STEIN {}".format(decor, decor))
run_time = [(afile, ) + measure_run_time(karger_stein, afile, num_calls, num_instances) for afile in gen]
print_table(run_time)
