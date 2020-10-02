import re
from collections import Counter
from nltk.corpus import stopwords #library used to filter out common english words to produce more meaningful output


def top_word_counts(text):
	stoplist = stopwords.words('english')
	stoplist.extend(["said", "gutenberg", "could", "would", "shall", "unto", "thou", "thy", "ye", "thee",])
	# stoplist.extend(list(range(0, 2000)))
	clean = []
	for word in re.split(r"\W+", text):
		if word not in stoplist:
			clean.append(word)
	top_10 = Counter(clean).most_common(10)
	return top_10
