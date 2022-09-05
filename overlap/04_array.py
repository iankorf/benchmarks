import sys

f2s = []
with open(sys.argv[2]) as fp:
	for line in fp.readlines():
		chrom, beg, end = line.split()
		f2s.append( (chrom, int(beg), int(end)) )

with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		c1, b1, e1 = line.split()
		b1 = int(b1)
		e1 = int(e1)
		for c2, b2, e2 in f2s:
			if c1 == c2 and b2 <= e1 and e2 >= b1:
				print(f'{c1}:{b1}-{e1} {c2}:{b2}-{e2}')
