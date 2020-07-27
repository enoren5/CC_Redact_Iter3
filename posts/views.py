from django.shortcuts import redirect, render, get_object_or_404
from posts.models import Posts

def posts(request):
    posts = Mortem.objects.all().order_by('-pub_date')
    context = {'posts':posts}
    return render(request, 'alls/landings.html', context)

