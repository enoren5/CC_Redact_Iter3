import operator
from django.shortcuts import redirect, render, get_object_or_404
from posts.models import Posts, PageView
from .utils import top_word_counts

def posts(request):
    # Based on Pankaj Mishra's SO answere here: https://stackoverflow.com/a/45411928/6095646
    # This is Pankaj Mishra's hit counter:
    if (PageView.objects.count()<=0):
        x = PageView.objects.create()
        x.save()
    else:
        x = PageView.objects.all()[0]
        x.hits = x.hits+1
        x.save()
    context = {'pages':x.hits}
    
    # The posts content:
    posts = Posts.objects.all().order_by('-pub_date')
    context.update({'posts':posts})
    post_string = ''
    for post in posts:
        post_string += post.body
    
    # Counting words of Alice.txt + posts content:
    post_words = top_word_counts(post_string.lower())
    alice_words = top_word_counts(
        open("counters/Bible.txt", "r").read().lower())

    context.update({
        'post_words': post_words,
        'alice_words': alice_words
    })

    return render(request, 'alls/landings.html', context)

