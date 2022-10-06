from files import files
from graph import karger_stein
from tqdm import tqdm
from test import measure_run_time
from representation import plot, print_table

# Mesure the runtime
run_times_karger = [(afile, ) + measure_run_time(karger_stein, afile, "karger_stein")
                    for afile in tqdm(files)]

print_table(run_times)
plot(run_times)
