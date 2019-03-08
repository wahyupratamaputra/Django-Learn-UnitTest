from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    if request.method == 'POST':
        return render(request, 'tdd/index.html', {'new_item_text': request.POST['item_text']})
    return render(request, 'tdd/index.html')