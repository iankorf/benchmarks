import sys

def read_features(file):
	with open(file) as fp:
		for line in fp.readlines():
			chrom, beg, end = line.split()
			yield chrom, int(beg), int(end)

for c1, b1, e1 in read_features(sys.argv[1]):
	for c2, b2, e2 in read_features(sys.argv[2]):
		if c1 == c2 and b2 <= e1 and e2 >= b1:
			print(f'{c1}:{b1}-{e1} {c2}:{b2}-{e2}')
