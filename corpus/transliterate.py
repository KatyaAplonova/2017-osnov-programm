import sys

lines = sys.stdin.readlines()

table = {}

fd = open('symbols.tsv')
for line in fd.readlines():
	line = line.strip('\n')
	line = line.split('\t')
	inn = line[0]
	out = line[1]
	table[inn] = out
for a in lines:
	a = a.strip()
	if a.count('\t') != 9:
		print(a)
		continue
	line = a.split('\t')
	form = line[1]
	for sym in table:
		form = form.replace(sym, table[sym])
	line[9] = form
	print('\t'.join(line))
