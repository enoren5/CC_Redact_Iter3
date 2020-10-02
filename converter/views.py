from django.shortcuts import render

def mile2km(request):
    if 'mile2km' in request.GET:
        mile = request.GET['mile2km']
        mile = float(mile) # cast mile value to float
        ratio = float(1.60934) 
        km = mile * ratio # output defined
        context = { "km" : km, "temp": True,}
        return render(request, 'alls/converter.html', context)
    else:
        return render(request, 'alls/converter.html', {"temp": False,}) 

def km2mile(request):
    if 'km2mile' in request.GET:
        km = request.GET['km2mile']
        km = float(km) # cast km value to float
        ratio = float(1.60934) 
        mile = km / ratio # output defined
        context = { "mile": mile, "temp": True,}
        return render(request, 'alls/converter.html', context)
    else:
        return render(request, 'alls/converter.html', {"temp": False,}) 
    
    