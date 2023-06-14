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
# VID 4 (One to Many) Step 7.1 -- Add FEEDING to models import
from .models import Cat, Feeding 




# Register your models here.
# Step 9.4 REGISTER our MODELS in admin.py
admin.site.register(Cat)
# VID 4 (One to Many) Step 7.2 -- REGISTER FEEDING
admin.site.register(Feeding)