import os
import subprocess
import sys
import time

def elapsed(cmd):
	t0 = time.perf_counter()
	subprocess.run(cmd, shell=True)
	t1 = time.perf_counter()
	sys.stderr.write(f'{t1 - t0} {cmd}\n')
	return t1 - t0

def bench(cmd, iterations):
	t = []
	for i in range(iterations):
		t.append(elapsed(cmd))
	return min(t)

TEST = {}

####################################################
# Test 1: Generate random sequences and count kmers
####################################################

# perl
os.environ['PERL5LIB'] = '../algorithms/perl'
rseq = '../algorithms/perl/randomseq 1000 1000'
kmer = '../algorithms/perl/kmerfreq -k 6 -'
TEST['t1.pl'] = bench(f'{rseq} | {kmer} > /dev/null', 1)

# python
rseq = '../algorithms/python/randomseq 1000 1000'
kmer = '../algorithms/python/kmerfreq -k 6 -'
TEST['t1.py'] = bench(f'{rseq} | {kmer} > /dev/null', 1)

# go, C

#########################
# Test 2: Smith-Waterman
#########################

# make some test sequences
seqs = '../algorithms/perl/randomseq 10 200'
subprocess.run(f'{seqs} > f1', shell=True)
subprocess.run(f'{seqs} > f2', shell=True)

# perl
sw = '../algorithms/perl/smithwaterman f1 f2'
TEST['t2.pl'] = bench(f'{sw} > /dev/null', 1)



#################
# Output Section
#################

for tid in TEST:
	print(tid, end='\t')
print('')

for tid in TEST:
	print(TEST[tid], end='\t')
print('')
