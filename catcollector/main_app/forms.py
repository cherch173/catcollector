# VID 4 (One to Many) STEP 9.0
# touch main_app/forms.py

# Step 9.1 Define the ModelForm
# forms.py

from django.forms import ModelForm
from .models import Feeding

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']
