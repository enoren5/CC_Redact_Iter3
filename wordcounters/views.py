from django.shortcuts import render
from collections import Counter
from nltk.corpus import stopwords
from .utils import top_word_counts, top_10

def wordcounters(request, text=""):
    post_text, alice_text = top_10()

    post_words = top_word_counts(post_text)
    alice_words = top_word_counts(alice_text)
    context = ({
        'post_words': post_words,
        'alice_words': alice_words
    })

    return context
    