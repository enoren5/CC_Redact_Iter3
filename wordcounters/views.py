from django.shortcuts import render
from collections import Counter
import re
from nltk.corpus import stopwords

def wordcounters(request, text=""):
    """
    This function processes the top 10 most common words in a text file and then renders them.
    """
    text = open("wordcounters/Alice.txt", "r").read().lower()
    stoplist = stopwords.words('english')
    stoplist.extend(["said","gutenberg", "could", "would",]) 
    clean = []
    for word in re.split(r"\W+",text):
        if word not in stoplist:
            clean.append(word)
    top_10 = Counter(clean).most_common(10)
    return render(request, 'alls/landings.html', {'top_10': top_10})