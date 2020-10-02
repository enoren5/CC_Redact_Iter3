from django.shortcuts import render

# Create your views here.
def mile2km(request):
    Mile = input("Enter the number of miles to convert to kilometers")
    Mile = float(Mile)
    KMratio = float(1.60934)
    KM = Mile * KMratio
    context = None
    return render(request, 'alls/mile2km.html', context) 