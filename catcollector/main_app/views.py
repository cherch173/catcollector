from django.shortcuts import render

# VID 3 (CBVs)
# Part 5 Step 4 IMPORT the CREATE VIEW
from django.views.generic.edit import CreateView

# VID 2 (Models) Step 8.0 IMPORT the CAT MODEL
from .models import Cat


# (VID 1 Baby Step) Part 10 Step 4) Code the View - add the cats!
# cats = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# VID 1 (Setup) Part 10 Step 4) Code the VIEW for INDEX PAGE
def cats_index(request):
    # VID 2 (Models) Step 8.1 INCLUDE the ALL METHOD to INDEX FUNCTION
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {
        'cats': cats
    })

# VID 2 (Models)
# Step 10.4 CODE the VIEW for DETAILS PAGE (Show Functionality)
    # DEFINE Addtl PARAMETERS to ACCEPT your NEW ARGUMENTS (passed in as KWARG)
def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', { 
        'cat': cat 
    })

# VID 3 (CBVs) 
# Part 5 Step 4.2 CODE the VIEW as a CLASS (not DEF) for CREATE (New Page)
class CatCreate(CreateView):
    model = Cat
    fields = '__all__'

# Part 5 Step 5.1 touch new/create template html using
# touch main_app/templates/main_app/cat_form.html