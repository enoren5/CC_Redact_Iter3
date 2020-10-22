from django.shortcuts import render
from blogs.models import Posts
from wordcounters.views import wordcounters

def converters(request):
    posts = Posts.objects.all().order_by('-pub_date')
    context = {'posts':posts}
    context.update(wordcounters(request))

    if 'km2mile' in request.GET:
        km = request.GET['km2mile']
        km = float(km) # cast km value to float
        ratio = float(1.60934) 
        mile = km / ratio # output defined
        context.update({ "mile": mile, 'selectConv': False, 'convmi': False, 'resultsmi': True})
        return render(request, 'alls/landings.html', context)
        
    elif 'mile2km' in request.GET:
        mile = request.GET['mile2km']
        mile = float(mile) # cast mile value to float
        ratio = float(1.60934) 
        km = mile * ratio # output defined
        context.update({ "km" : km, 'selectConv': False, 'convkm': False, 'resultskm': True})
        return render(request, 'alls/landings.html', context)

    elif 'conversion' in request.GET:
        conversion = request.GET['conversion']
        if conversion == 'km2mile':
            context.update({'selectConv': False, 'convkm': True, 'convmi': False})
            return render(request, 'alls/landings.html', context)
        elif conversion == 'mile2km':
            context.update({'selectConv': False, 'convkm': False, 'convmi': True})
            return render(request, 'alls/landings.html', context)

