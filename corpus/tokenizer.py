import sys
text = sys.stdin.readlines()
sentence_1 = 1
for line in text
	print('#sent_id =', sentence_id)
	token = 1
	punctuation = ['.',',','?','!']
	for symbols in ponctuation:
		line = line.replace(symbols, ' ' + symbols)
	tokens = line.split(' ')
	for token in tokens
		print('%d\t%s' % (token))
		token = token + 1


