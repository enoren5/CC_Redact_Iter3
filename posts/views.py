import operator
from django.shortcuts import redirect, render, get_object_or_404
from posts.models import Posts
from .utils import top_word_counts

def posts(request):
    posts = Posts.objects.all().order_by('-pub_date')
    context = {'posts':posts}

    post_string = ''
    for post in posts:
        post_string += post.body

    post_words = top_word_counts(post_string.lower())
    alice_words = top_word_counts(
        open("counters/Alice.txt", "r").read().lower())

    context.update({
        'post_words': post_words,
        'alice_words': alice_words
    })

    return render(request, 'alls/landings.html', context)

