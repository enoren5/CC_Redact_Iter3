from django.shortcuts import render
from blogs.models import Posts
from blogs.views import BlogWordsCount
def home(request):
    if 'ccEntry' in request.GET:
        number = request.GET['ccEntry']
        redacted_num = 'xxxx xxxx {}'.format(number[-4:])
        posts = Posts.objects.all().order_by('-pub_date')
        context = BlogWordsCount()

        context.update(
            {'number':number, 'redacted_num':redacted_num, 'posts':posts, "temp": True}, 
        )
        return render(request, 'alls/landings.html', context )
    else:
        return render(request, 'alls/landings.html',{"temp": False})

def redactors(request):
    return render(request, 'alls/landings.html')
