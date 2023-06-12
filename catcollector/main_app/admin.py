# VID 2 (Models) Step 9 - ADMIN PRIVILEGES

# Step 9.1 CREATE a SUPERUSER
# in your terminal enter:
# python3 manage.pr createsuperuser

# enter username
# leave email blank for novelty projects
# enter password you can remember cause you can't see it

# if you mess up use python3 manage.py changepassword <user_name>
# to CHANGE or UPDATE your password

from django.contrib import admin
# import your models here

# Step 9.3 IMPORT your MODEL
from .models import Cat 




# Register your models here.
# Step 9.4 REGISTER our MODELS in admin.py
admin.site.register(Cat)