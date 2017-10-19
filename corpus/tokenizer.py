import sys
sent_id = 1
lines = sys.stdin.readlines()

for line in lines:	
	if line.strip() == '':
		continue
	print('# sent_id = :%d' % (sent_id))
	print('# text = %s' % (line.text.strip()))
	tok_id = 1
	punctuation = ['߸',':','(',')',':','?']
	for symbols in punctuation:
#in the text there are french titles and extra new lines, probably, we should ignore french words and delete extra new lines?..	
		line = line.replace(symbols, ' ' + symbols)
	tokens = line.split(' ')
	for token in tokens:
		print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % ((tok_id, token), '_', '_', '_', '_', '_', '_', '_')
		tok_id = tok_id + 1
	count_tok = count_tok + 1
	print('')
	sent_id = sent_id + 1
