import sys
import xml.etree.ElementTree as ET

def get_udtags(lem, pos, gloss):
	""" Convert a tuple of (lemma, part-of-speech, gloss) to a UD part-of-speech
	    tag and a list of morphological features """
	tags = ['X', []]

	if lem in ',!?:;.':
		return ['PUNCT', ['_']]
	if pos == 'adj':
		tags[0] = 'ADJ'
	if pos == 'adv':
		tags[0] = 'ADV' 
	if pos == 'adv.p':
		tags[0]='ADV'
	if pos == 'adv.ex':
		tags[0] = 'ADV'  
	if pos == 'num':
		tags[0] = 'NUM' 
	if pos == 'n':
		tags[0] = 'NOUN' 
	if pos == 'n.prop':
		tags[0] = 'PROPN' 
	if pos == 'v':
		tags[0] = 'VERB'
	if pos == 'vq':
		tags[0] ='VERB'
	if pos == 'ptcp':
		tags[0] ='VERB'
	if pos == 'pers':	
		tags[0] = 'PRON' 
		tags[1].append('PronType=Prs')
	if pos == 'pron':
		tags[0] = 'PRON' 
	if pos == 'pm':
		tags[0] = 'AUX'
	if pos == 'pp':
		tags[0] = 'ADP'
	if pos == 'dtm':
		tags[0] = 'DET'  
	if pos == 'prt':
		tags[0] = 'PART'
	if pos == 'conj' and lem in ["bàri", "jàa", "jàga", "kélen", "kòni", "nká", "nk'", "ô", "ôo", "wô", "tàrí", "tɛ̀rí", "wà", "wáa", "w'", "wálà", "wàlámà", "wàlímà", "wáli", "wó"]:
		tags[0] = 'CCONJ'
	if pos == 'conj' and lem in ["bárì", "bárìsá", "bárì sá", "báwò", "bɛ́ɛ", "bína", "bíɲa", "dàma", "dɔ́rɔn", "jànkó", "jàngó", "kàsɔrɔ", "kàtugu", "kàtuguni", "kɔ́ntɛ̀", "mînkɛ́", "mînkɛ́ni", "ní", "n'ó tɛ́", "nóntɛ́", "nɔ́ntɛ", "sá", "sábu", "sáabu", "sábi", "sábula", "sàfɛ", "sánì", "sánni", "sán'", "sánn'", "sànkó", "sàngó", "tɛ́sɛ", "tílen", "wálasa", "wáasa", "wálisa", "yáa", "yála", "yálasa", "yáasa", "yála", "yálisa", "jáasa", "yànni", "yànn'", "yàli"]:
		tags[0] = 'SCONJ'
	if pos == 'cop':
		tags[0] = 'AUX'
	if gloss == 'ABR':
		tags[1].append('Abbr=Yes') 
	if gloss == 'REL.PL2':
		tags[1].append('PronType=Rel')
		tags[1].append('Number=Plur') 
	if gloss == 'REL':
		tags[1].append('PronType=Rel')
	if gloss == 'PFV.TR':
		tags[1].append('Aspect=Perf')
		tags[1].append('Valency=2')
	if gloss == 'SBJV':
		tags[1].append('Mood=Sub')
	if gloss == 'REFL':
		tags[1].append('Reflexive=Yes')
	if gloss == 'RECP':
		tags[1].append('PronType=Rcp')
	if gloss == 'QUAL.NEG':
		tags[1].append('Polarity=Neg')
	if gloss == 'QUAL.AFF':
		tags[1].append('Polarity=Pos')
	if gloss == 'PST':
		tags[1].append('Tense=Past')
	if gloss == 'PROH':
		tags[1].append('Polarity=Neg')
		tags[1].append('Mood=Imp')
	if gloss == 'PROG.NEG':
		tags[1].append('Polarity=Neg')
		tags[1].append('Aspect=Prog')
	if gloss == 'PROG.AFF':
		tags[1].append('Polarity=Aff')
		tags[1].append('Aspect=Prog')
	if gloss == 'PFV.NEG':
		tags[1].append('Polarity=Neg')
		tags[1].append('Aspect=Perf')
	if gloss == 'ORD':
		tags[1].append('NumType=Ord')
	if gloss == 'IPFV.NEG':
		tags[1].append('Polarity=Neg')
		tags[1].append('Aspect=Imp')
	if gloss == 'IPFV.AFF':
		tags[1].append('Polarity=Aff')
		tags[1].append('Aspect=Imp')
	if gloss == 'INFR.NEG':
		tags[1].append('Evident=Infer')
		tags[1].append('Polarity=Neg')
	if gloss == 'INFR':
		tags[1].append('Evident=Infer')
	if gloss == 'IMP':
		tags[1].append('Mood=Imp')
	if gloss == 'FUT.NEG':
		tags[1].append('Polarity=Neg')
		tags[1].append('Tense=Fut')
	if gloss == 'FUT':
		tags[1].append('Tense=Fut')
	if gloss == 'COP.NEG':
		tags[1].append('Polarity=Neg')
	if gloss == 'COND.NEG':
		tags[1].append('Mood=Cnd')
		tags[1].append('Polarity=Neg')
	if gloss == 'COND.AFF':
		tags[1].append('Mood=Cnd')
		tags[1].append('Polarity=Aff')
	if gloss == '3SG.EMPH':
		tags[1].append('Number=Sing')
		tags[1].append('Person=3')
		tags[1].append('PronType=Emp')
	if gloss == '2SG.EMPH':
		tags[1].append('Number=Sing')
		tags[1].append('Person=2')
		tags[1].append('PronType=Emp')
	if gloss == '2PL.EMPH':
		tags[1].append('Number=Plur')
		tags[1].append('Person=2')
		tags[1].append('PronType=Emp')
	if gloss == '1SG.EMPH':
		tags[1].append('Number=Sing')
		tags[1].append('Person=1')
		tags[1].append('PronType=Emp')
	if gloss == '1PL.EMPH':
		tags[1].append('Number=Plur')
		tags[1].append('Person=1')
		tags[1].append('PronType=Emp')
	if gloss == '3SG':
		tags[1].append('Number=Sing')
		tags[1].append('Person=3')
	if gloss == '3PL':
		tags[1].append('Number=Plur')
		tags[1].append('Person=3')
	if gloss == '2SG':
		tags[1].append('Number=Sing')
		tags[1].append('Person=2')
	if gloss == '1SG':
		tags[1].append('Number=Sing')
		tags[1].append('Person=1')
	if gloss == '2PL':
		tags[1].append('Number=Plur')
		tags[1].append('Person=2')
	if gloss == '1PL':
		tags[1].append('Number=Plur')
		tags[1].append('Person=1')
	if tags[1] == []:
		tags[1] = ['_']

	return tags
def get_val(token, tip, attr):
	""" Return the value of a specific kind of subelement"""
	# .//span[@class="lemma"]
	# .//sub[@class="ps"]
	val = token.findall('.//'+tip+'[@class="'+attr+'"]')
	if len(val) > 0:
		return val[0].text
	else:
		return '_'

# Load the HTML file
tree = ET.parse(sys.argv[1])
root = tree.getroot()

# Set the token count to 0
count_tok = 0

# Set the document ID to the name of the file
doc_id = sys.argv[1]
# Set the sentence ID to 1
sent_id = 1

# For each of the sentences in the file
for sent in root.findall('.//span[@class="sent"]'):
	# If the sentence has some kind of HTML tag in, skip it.
	if sent.text.count('<h') > 0:
		continue
	# Print out the sentence ID and the original text as a comment
	print('# sent_id = %s:%d' % (doc_id, sent_id))
	print('# text = %s' % (sent.text.strip()))
	tok_id = 1
	# Find all the tokens in the sentence
	tokens = sent.findall(".//span")
	for token in tokens:
		# What kind of token are we looking at?
		klass = token.attrib["class"] 
		# If the token is not punctuation or a word then skip it.
		if klass != 'c' and klass != 'w': 
			continue
		# The word form is the contents of the span
		w = token.text
		# Get the language-specific part-of-speech tag and the gloss
		xpos = get_val(token, 'sub', 'ps');
		gloss = get_val(token, 'sub', 'gloss');
		# If the type of token is punctuation, then the lemma is the 
		# same as the surface form
		if klass == 'c':
			lem = w
			gloss = w
		else:
			lem = get_val(token, 'span', 'lemma')
		# Get the universal part of speech and list of features
		(upos, feats) = get_udtags(lem, xpos, gloss);
		# Print out the token line
		print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (tok_id, w, lem, upos, xpos, '|'.join(feats), '_', '_', '_','Gloss='+gloss))
		# Increment the token id by 1
		tok_id = tok_id + 1
		count_tok = count_tok + 1
	print('')
	sent_id = sent_id + 1

# Print out the number of sentences and tokens as debugging information
print(sent_id, count_tok, file=sys.stderr)
