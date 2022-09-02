import sys

def read_features(file):
	features = []
	with open(file) as fp:
		for line in fp.readlines():
			chrom, beg, end = line.split()
			features.append( (chrom, int(beg), int(end)) )
	return features

def overlaps(f1, f2):
	c1, b1, e1 = f1
	c2, b2, e2 = f2
	if c1 == c2 and b2 <= e1 and e2 >= b1: return True
	return False

f1s = read_features(sys.argv[1])
f2s = read_features(sys.argv[2])

for f1 in f1s:
	for f2 in f2s:
		if overlaps(f1, f2):
			c1, b1, e1 = f1
			c2, b2, e2 = f2
			print(f'{c1}:{b1}-{e1} {c2}:{b2}-{e2}')
