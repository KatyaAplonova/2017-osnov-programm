import sys

lines = sys.stdin.readlines()
	print('#', line)
for i in range (0,len(text)):
	line = text[i].strip()
	if line == "":
		continue
	print("#sent_id =", i+1, "\n"+"#text=", line)
	token_id = 1
	punctuation = [".",",","?","!",";"]
	for symbols in punctuation:
		line = line.replace(symbols, ' ' + symbols)
	sentence_id = line.split(' ')
	tokens = line.split(" ") 
	for token in tokens:
		print((token_id, token)\t_\t_\t_\t_\t_\t_\t_\t_)
		token_id = token_id + 1
	print()


