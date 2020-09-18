import operator
from django.shortcuts import redirect, render, get_object_or_404
from posts.models import Posts
from .utils import word_counts

def posts(request):
    posts = Posts.objects.all().order_by('-pub_date')
    context = {'posts':posts}

    post_string = ''
    for post in posts:
        post_string += post.body

    words = word_counts(post_string)

    paginated_max = 10
    paginated_min = 0
    page_prev = 0
    page_next = 2
    if request.GET.get('p') and not request.GET.get('p') == 1:
        paginated_max = int(request.GET.get('p') + '0')
        paginated_min = paginated_max - 10

        page_next = int(request.GET.get('p')) + 1
        page_prev = int(request.GET.get('p')) - 1

    words = dict(sorted(words.items(), key=operator.itemgetter(1), reverse=True)[paginated_min:paginated_max])

    context.update({
        'words': words,
        'page_prev': page_prev,
        'page_next': page_next
    })

    return render(request, 'alls/landings.html', context)

