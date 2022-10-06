from rapresentation import ks_complex, plot, read_csv

res = read_csv("karger_stein_results.txt")
plot(res, f=ks_complex, alg_name="karger_stein")
