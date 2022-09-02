import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1) as fp1:
	for line1 in fp1.readlines():
		c1, b1, e1 = line1.split()
		b1 = int(b1)
		e1 = int(e1)

		with open(file2) as fp2:
			for line2 in fp2.readlines():
				c2, b2, e2 = line2.split()
				if c1 == c2:
					b2 = int(b2)
					e2 = int(e2)
					if b2 <= e1 and e2 >= b1:
						print(f'{c1}:{b1}-{e1} {c2}:{b2}-{e2}')
