import operator
from django.shortcuts import redirect, render, get_object_or_404
from blogs.models import Posts, PageView
from .utils import top_word_counts
from wordcounters.views import wordcounters

def posts(request):
    # Based on Pankaj Mishra's SO answere here: https://stackoverflow.com/a/45411928/6095646
    # This is Pankaj Mishra's hit counter:
<<<<<<< HEAD
    context = BlogWordsCount(request)

    return render(request, 'alls/landings.html', context)

def BlogWordsCount(request):
=======
    context = BlogWordsCount()

    return render(request, 'alls/landings.html', context)

def BlogWordsCount():
>>>>>>> 89443c0c9c06786c26c20fe27653365ca9cd51f0

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

    context.update(wordcounters(request))

<<<<<<< HEAD
    return context
    
=======
    return render(request, 'alls/landings.html', context)
>>>>>>> 89443c0c9c06786c26c20fe27653365ca9cd51f0
