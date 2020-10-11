from django.shortcuts import render
from blogs.models import Posts
from blogs.views import BlogWordsCount
def home(request):
    if 'ccEntry' in request.GET:
        number = request.GET['ccEntry']
        redacted_num = 'xxxx xxxx {}'.format(number[-4:])
        posts = Posts.objects.all().order_by('-pub_date')
<<<<<<< HEAD
        context = BlogWordsCount(request)
=======
        context = BlogWordsCount()
>>>>>>> 89443c0c9c06786c26c20fe27653365ca9cd51f0

        context.update(
            {'number':number, 'redacted_num':redacted_num, 'posts':posts, "temp": True}, 
        )
        return render(request, 'alls/landings.html', context )
    else:
        return render(request, 'alls/landings.html',{"temp": False})

def redactors(request):
    return render(request, 'alls/landings.html')
