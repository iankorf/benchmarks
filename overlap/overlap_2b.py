import sys

def read_features(file):
	features = []
	with open(file) as fp:
		for line in fp.readlines():
			chrom, beg, end = line.split()
			features.append( (chrom, int(beg), int(end)) )
	return features

f2s = read_features(sys.argv[2])

with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		c1, b1, e1 = line.split()
		b1 = int(b1)
		e1 = int(e1)
		for c2, b2, e2 in f2s:
			if c1 == c2 and b2 <= e1 and e2 >= b1:
				print(f'{c1}:{b1}-{e1} {c2}:{b2}-{e2}')
