from django.shortcuts import render
from collections import Counter
from blogs.models import Posts
from nltk.corpus import stopwords
from blogs.utils import top_word_counts

def wordcounters(request, text=""):
    """
    This function processes the top 10 most common words in a text file and then renders them.
    """
    posts = Posts.objects.all().order_by('-pub_date')

    post_string = ''
    for post in posts:
        post_string += post.body

    post_text = post_string.lower()

    alice_text = open("wordcounters/Alice.txt", "r").read().lower()

    top_10 = top_word_counts(post_text + alice_text)

    return render(request, 'alls/landings.html', {'top_10': top_10})