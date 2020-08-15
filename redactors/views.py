from django.shortcuts import render
# from posts.views import context
from posts.models import Posts

def redactors(request):
    return render(request, 'alls/landings.html')

def home(request):
    if 'ccEntry' in request.GET:
        number = request.GET['ccEntry']
        redacted_num = 'xxxx xxxx {}'.format(number[-4:])
        posts = Posts.objects.all().order_by('-pub_date')
        # context = {'posts':posts}
        return render(request, 'alls/landings.html', {'number':number, 'redacted_num':redacted_num, 'posts':posts, })
    else:
        return render(request, 'alls/landings.html')

def results(request):
     return render(request, 'alls/landings.html')
