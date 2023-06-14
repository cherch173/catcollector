from django.shortcuts import render

# VID 3 (CBVs)
# Part 5 Step 4 IMPORT the CREATE VIEW
# Part 6 Step 3 add UPDATE & VIEW to existing VIEWS IMPORT
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# VID 2 (Models) Step 8.0 IMPORT the CAT MODEL
from .models import Cat
# VID #5 (One to Many) Part 9.2
# IMPORT the FEEDING Model Form
from .forms import FeedingForm



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
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {
    # include the cat and feeding_form in the context
    'cat': cat, 'feeding_form': feeding_form
  })

# VID 3 (CBVs) 
# Part 5 Step 4.2 CODE the VIEW as a CLASS (not DEF) for CREATE (New Page)
class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    # Part 5 Step 5.5 if you want an easy redirect for your newly created cat
    # functionality you can enter a SUCCESS URL to an explicit id
    # (example)
    # success_url = '/cats/{cat_id}'
    # or just to the index
    success_url = '/cats'

# Part 5 Step 5.1 touch new/create template html using
# touch main_app/templates/main_app/cat_form.html

# Part 6 Step 4.1 ADD the VIEW for UPDATE
class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']
    success_url = '/cats'
# Part 6 Step 4.2 ADD the VIEW for DELETE
class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats'