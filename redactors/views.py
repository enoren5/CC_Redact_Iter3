from django.shortcuts import render
from blogs.models import Posts

def home(request):
    if 'ccEntry' in request.GET:
        number = request.GET['ccEntry']
        redacted_num = 'xxxx xxxx {}'.format(number[-4:])
        posts = Posts.objects.all().order_by('-pub_date')
        # context = {'posts':posts}
        return render(request, 'alls/landings.html', {'number':number, 'redacted_num':redacted_num, 'posts':posts, "temp": True,})
    else:
        return render(request, 'alls/landings.html',{"temp": False})

def redactors(request):
    return render(request, 'alls/landings.html')
