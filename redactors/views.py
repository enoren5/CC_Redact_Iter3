from django.shortcuts import render

# Create your views here.
def redactors(request):
    return render(request, 'alls/landings.html')

def home(request):
    if 'ccEntry' in request.GET:
        number = request.GET['ccEntry']
        redacted_num = 'xxxx xxxx xxxx {}'.format(number[-4:])
        return render(request, 'alls/results.html', {'number':number, 'redacted_num':redacted_num})
    else:
        return render(request, 'alls/landings.html')

def results(request):
     return render(request, 'alls/results.html')
