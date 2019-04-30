from django.shortcuts import render

def home_view(request):
    """Home Route."""

    return render(request, 'generic/home.html')
