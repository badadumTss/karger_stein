from files import files
from karger_stein import karger_stein
from stoer_wagner import stoer_wagner
from hybrid import hybrid
from tqdm import tqdm
from test import measure_run_time
from rapresentation import ks_complex, plot, plot3D, print_table, sw_complex
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
    gen = tqdm(frange)
    print("\n{} KARKGER AND STEIN {}".format(decor, decor))
    ks_run = [(afile, ) + measure_run_time(karger_stein, afile, "karger_stein_scratch") for afile in gen]
    plot(ks_run, 'Karger and Stein', ks_complex)

# Stoer and Wagner
if not args.no_sw:
    gen = tqdm(frange)
    print("{} STOER AND WAGNER {}".format(decor, decor))
    sw_run = [(afile, ) + measure_run_time(stoer_wagner, afile, "stoer_wagner_scratch") for afile in gen]
    plot3D(sw_run, 'Stoer and Wagner', sw_complex)

# Hybrid
if not args.no_hy:
    gen = tqdm(frange)
    print("{} Hybrid {}".format(decor, decor))
    hy_run = [(afile, ) + measure_run_time(hybrid, afile, "hybrid_scratch", 1) for afile in gen]
    plot3D(hy_run, 'Hybrid', sw_complex)

if not args.no_ks:
    print_table(ks_run)
if not args.no_sw:
    print_table(sw_run)
if not args.no_hy:
    print_table(hy_run)
