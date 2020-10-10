import re
from collections import Counter
from nltk.corpus import stopwords #library used to filter out common english words to produce more meaningful output
from blogs.models import Posts

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

def top_10():
    """
    This function processes the top 10 most common words in a text file and then renders them.
    """
    posts = Posts.objects.all().order_by('-pub_date')

    post_string = ''
    for post in posts:
        post_string += post.body

    post_text = post_string.lower()

    alice_text = open("wordcounters/Alice.txt", "r").read().lower()

    return post_text, alice_text
    