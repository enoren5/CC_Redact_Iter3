import re
from collections import Counter
from nltk.corpus import stopwords


def top_word_counts(text):
	# text = open("counters/Alice.txt", "r").read().lower()

	stoplist = stopwords.words('english')
	stoplist.extend(["said", "gutenberg", "could", "would", ])
	clean = []
	for word in re.split(r"\W+", text):
		if word not in stoplist:
			clean.append(word)
	top_10 = Counter(clean).most_common(10)

	return top_10
