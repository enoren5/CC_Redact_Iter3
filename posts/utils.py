import re

def word_counts(data):

	delimeters = ['.', ',', '?', '<', '>', '/', ';', ':', '|', '{', '}',
				  '[', ']', '!', '@', '#', '$', '%', '^', '&', "*",  '(', ')',
				  '-', '+', '_', '=' '\r']

	data = data.replace('\r', ' ').replace('\n', ' ')
	for rm in delimeters:
		data = data.replace(rm, '')


	words = data.split(' ')

	counts = {}
	for word in words:
		if counts.get(word):
			counts[word] = counts.get(word) + 1
		else:
			counts.update({
				word: 1
			})

	return counts
