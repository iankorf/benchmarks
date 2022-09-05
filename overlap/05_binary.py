import sys
import json

def cmp_features(f1, f2):
	c1, b1, e1 = f1
	c2, b2, e2 = f2

	if c1 != c2:
		if c1 < c2: return -1
		if c1 > c2: return +1

	if e1 < b2: return -1
	if b1 > e2: return +1

	return 0

def matching_features(feats, f, max_fsize):
	idx = find_one_overlap_binary(feats, f)
	if idx is None: return []

	lo = 0
	for i in range(idx, -1, -1):
		c1, b1, e1 = f
		c2, b2, e2 = feats[i]
		if c1 < c2:
			lo = i
			break
		if c1 == c2 and e2 - b1 > max_fsize:
			lo = i
			break

	hi = len(feats) -1
	for i in range(idx, len(feats)):
		c1, b1, e1 = f
		c2, b2, e2 = feats[i]
		if c2 > c1:
			hi = i
			break
		if c1 == c2 and b2 - e1 > max_fsize:
			hi = i
			break

	found = []
	for i in range(lo, hi+1):
		if cmp_features(f, feats[i]) == 0:
			found.append(feats[i])

	return found

def find_one_overlap_binary(feats, f1):
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
		if (lo, idx, hi) == last: # terminating...
			# can be one off hi or lo, or the last feature
			if cmp_features(f1, feats[idx-1]) == 0: return idx -1
			if cmp_features(f1, feats[idx+1]) == 0: return idx +1
			if cmp_features(f1, feats[hi])    == 0: return hi
			break

		last = (lo, idx, hi)

	return None


feats = []
with open(sys.argv[2]) as fp:
	for line in fp.readlines():
		chrom, beg, end = line.split()
		feats.append( (chrom, int(beg), int(end)) )
feats = sorted(feats, key=lambda x:(x[0], x[1], x[2]))

max_fsize = 1000 # ugh

with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		chrom, beg, end = line.split()
		f1 = (chrom, int(beg), int(end))
		for f2 in matching_features(feats, f1, max_fsize):
			c2, b2, e2 = f2
			print(f'{chrom}:{beg}-{end} {c2}:{b2}-{e2}')
