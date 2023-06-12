from django.shortcuts import render

# VID 2 (Models) Step 8.0 IMPORT the CAT MODEL
from .models import Cat

# (Baby Step) Part 10 Step 4) Code the View - add the cats!
# cats = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# VID 1 (Setup) Part 10 Step 4) Code the View
def cats_index(request):
    # VID 2 (Models) Step 8.1 INCLUDE the ALL METHOD to INDEX FUNCTION
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {
        'cats': cats
    })

