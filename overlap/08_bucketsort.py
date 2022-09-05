import sys

def read_features(file):
	features = {}
	with open(file) as fp:
		for line in fp.readlines():
			chrom, beg, end = line.split()
			beg = int(beg)
			end = int(end)
			if chrom not in features: features[chrom] = []
			if len(features[chrom]) < end:
				while True:
					features[chrom].append([])
					if len(features[chrom]) == end: break
			for i in range(beg -1, end):
				features[chrom][i].append( (beg, end) )
	return features

def overlaps(f1, f2):
	b1, e1 = f1
	b2, e2 = f2
	if b2 <= e1 and e2 >= b1: return True
	return False

f2b = read_features(sys.argv[2])

with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		chrom, beg, end = line.split()
		beg = int(beg)
		end = int(end)
		found = {}
		if chrom in f2b:
			for i in range(beg, end):
				try:
					if len(f2b[chrom][i]) != 0:
						for f2 in f2b[chrom][i]:
							found[f2] = True
				except IndexError:
					pass
		if found:
			for f2 in found:
				b2, e2 = f2
				print(f'{chrom}:{beg}-{end} {chrom}:{b2}-{e2}')
