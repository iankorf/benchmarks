import sys
import json

def read_features(file):
	features = []
	with open(file) as fp:
		for line in fp.readlines():
			chrom, beg, end = line.split()
			features.append( (chrom, int(beg), int(end)) )

	return sorted(features, key=lambda x:(x[0], x[1], x[2]))

def overlaps(f1, f2):
	c1, b1, e1 = f1
	c2, b2, e2 = f2
	if c1 == c2 and b2 <= e1 and e2 >= b1: return True
	return False

def cmp_features(f1, f2):
	c1, b1, e1 = f1
	c2, b2, e2 = f2

	if c1 != c2:
		if c1 < c2: return -1
		if c1 > c2: return +1

	if e1 < b2: return -1
	if b1 > e2: return +1

	return 0

def overlap_index(feats, f1):
	hi = len(feats) -1
	lo = 0
	idx = (hi + lo) // 2
	last = (lo, idx, hi)

	while True:
		f2 = feats[idx]
		c = cmp_features(f1, f2)
		if   c < 0: hi = (hi + idx) // 2
		elif c > 0: lo = (lo + idx) // 2
		else: return idx

		idx = (hi + lo) // 2
		if (lo, idx, hi) == last: # ugly, is there a better way?
			if hi == len(feats) -1 and cmp_features(f1, feats[hi]) == 0:
				return hi
			break
		last = (lo, idx, hi)

	return -1

def find_overlaps(feats, f):
	idx = overlap_index(feats, f)
	if idx == -1: return []

	lo = None
	for i in range(idx, -1, -1):
		if cmp_features(f, feats[i]) == 0: lo = i
		else: break

	hi = None
	for i in range(idx, len(feats)):
		if cmp_features(f, feats[i]) == 0: hi = i
		else: break

	# make a final check to see if anything got missed

	for idx in range(lo, hi+1):
		yield feats[idx]

feats = read_features(sys.argv[2])
#for f in feats:
#	print(f)

def output(f1, f2):
	c1, b1, e1 = f1
	c2, b2, e2 = f2
	print(f'{c1}:{b1}-{e1} {c2}:{b2}-{e2}')

with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		chrom, beg, end = line.split()
		f1 = (chrom, int(beg), int(end))
		for f2 in find_overlaps(feats, f1):
			output(f1, f2)

# 2575 is the correct number
