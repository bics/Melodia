from django.shortcuts import render

# Create your views here.
def artist(request):
    return render(request, 'artist.html')