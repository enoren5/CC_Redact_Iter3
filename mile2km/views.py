from django.shortcuts import render

def mile2km(request):
    if 'mile2km' in request.GET:
        mile = request.GET['mile2km']
        mile = float(mile) # cast mile value to float
        ratio = float(1.60934) 
        km = mile * ratio # output defined
        context = {"km":km}
        return render(request, 'alls/results.html', context)
    else:
        return render(request, 'alls/mile2km.html') 

    # collect mile input from client somehow
    
    