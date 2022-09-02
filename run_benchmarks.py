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

# generate random sequence


t1 = bench('python3 ../algorithms/python/randomseq 1 100 > /dev/null')
print(t1)
