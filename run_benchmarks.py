import subprocess
import time

def elapsed(cmd):
	t0 = time.perf_counter()
	subprocess.run(cmd, shell=True)
	t1 = time.perf_counter()
	return t1 - t0

def bench(cmd):
	t = []
	for i in range(10):
		t.append(elapsed(cmd))
	return min(t)

# test1: generate random sequences


t1 = bench('python3 ../algorithms/python/randomseq 1 100 > /dev/null')
print(t1)


# test2: compute kmer frequencies


# test3: find longest ORF

# test4: dust

# test5: smithwaterman

# test6: viterbi

# test7: io

