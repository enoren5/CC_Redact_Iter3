from django.db import models

''' def redactors(request):
    return render(request, 'redactors/simon.html')

def home(request):
    if 'ccEntry' in request.GET:
        number = request.GET['ccEntry']
        redacted_num = 'xxxx xxxx xxxx {}'.format(number[-4:])
        return render(request, 'result.html', {'number':number, 'redacted_num':redacted_num})
    else:
        return render(request, 'alls/landings.html')

def result(request):
     return render(request, 'alls/results.html')
    '''