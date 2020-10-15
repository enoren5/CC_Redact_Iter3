import re
from collections import Counter
from nltk.corpus import stopwords #library used to filter out common english words to produce more meaningful output
from blogs.models import Posts

def top_word_counts(text):
	stoplist = stopwords.words('english')
	stoplist.extend(["said", "gutenberg", "could", "would", "shall", "unto", "thou", "thy", "ye", "thee","upon", "hath","came", "come","things", "also", "saying", "say"])
	# Added the mechanism to extend the list to include integers between 0 and 1999
	extendinteger = list(range(0, 2000))
	# Using map() it will convert the given type with one by iterations
	# of the array and convert to the corresponding type
	stoplist.extend(list(map(str,extendinteger)))
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

    alice_text = open("wordcounters/Bible.txt", "r").read().lower()

    return post_text, alice_text
    