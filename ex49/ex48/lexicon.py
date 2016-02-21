lexicon = {
	'north': 'direction',
	'south': 'direction',
	'east': 'direction',
	'west': 'direction'
}


def scan(sentence):
	words = sentence.split()
	result = []

	for word in words:
		pair = (lexicon[word], word)
		result.append(pair)

	return result
