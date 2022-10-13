from files import files
from test import measure_run_time, test_sw, test_ks, test_hy
from rapresentation import ks_complex, plot, plot3D, print_table, sw_complex
from datetime import datetime
import random
random.seed(datetime.now())
import argparse

parser = argparse.ArgumentParser(description='Run Karger and Stein and/or Stoer and Wagner alogirthms on the inputs in the `dataset` folder.')
parser.add_argument('--no-ks', dest='no_ks', action='store_true',
                    help='disable Karger and Stein algorithm (default: run)')
parser.add_argument('--no-sw', dest='no_sw', action='store_true',
                    help='disable Stoer and Wagner algorithm (default: run)')
parser.add_argument('--no-hy', dest='no_hy', action='store_true',
                    help='disable Hybrid algorithm (default: run)')
parser.add_argument('--start', dest='r_start', default=0,
                    help='start of the files to parse')
parser.add_argument('--end', dest='r_end', default=len(files),
                    help='end of the files to parse')

args = parser.parse_args()
print(args)

# misura il runtime
decor = '='*10
frange = files[int(args.r_start):int(args.r_end)]

ks_run = []
sw_run = []
hy_run = []

# Karger Stein
if not args.no_ks:
    print("\n{} KARKGER AND STEIN START {}".format(decor, decor))
    ks_run = measure_run_time(test_ks, frange)
    print("\n{} KARKGER AND STEIN DONE  {}".format(decor, decor))
    print_table(ks_run)
    plot(ks_run, 'Karger and Stein', ks_complex)

# Stoer and Wagner
if not args.no_sw:
    print("{} STOER AND WAGNER START {}".format(decor, decor))
    sw_run = measure_run_time(test_sw, frange, 1)
    print("\n{} STOER AND WAGNER DONE  {}".format(decor, decor))
    plot3D(sw_run, 'Stoer and Wagner', sw_complex)

# Hybrid
if not args.no_hy:
    print("{} Hybrid {}".format(decor, decor))
    hy_run = measure_run_time(test_hy, frange)
    plot3D(hy_run, 'Hybrid', sw_complex)

if not args.no_ks:
    print_table(ks_run)
if not args.no_sw:
    print_table(sw_run)
if not args.no_hy:
    print_table(hy_run)
