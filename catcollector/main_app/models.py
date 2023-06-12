from django.db import models

# Create your models here.

# VID 2 (Models) Step 5.0
# First, DEFINE your MODEL as a class (capitliaze so you know its a class)
class Cat(models.Model):
    # Step 5.1 add FIELDS (charField lol Garfield, cat puns)
    # use CharField for a small text input
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    # use TextField when you want a longer text input (multi line entry)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # use DecimalField for MONEY or MONETARY VALUE


# VID 2 (Models) Step 6.0 MIGRATIONS
# make MIGRATIONS to update the database with your new MODEL
# be very very CAREFUL as this can cause a loss of data if done compulsively

# Step 6.1 -- SHOW MIGRATIONS
# show migrations to see what needs to be updated
# python3 manage.py showmigrations

# Step 6.2 -- RUN MIGRATIONS
# run migrations to link new MODEL to DATABASE
# python3 manage.py migrate

# if done correctly you'll get rad green OK messages
# and a 0001_initial file in your migrations directory

# VID 2 (Models) Step 7.0 ORM

# Step 7.1 use ORM to CRUD Data in a PYTHON INTERACTIVE SHELL
# python3 manage.py shell
# this will load a >>> prompt meaning ORM is active

# Step 7.2 IMPORT model to DB
# >>> from main_app.models import Cat
# test by pressing enter

# Step 7.3 RETRIEVE all OBJECTS using all()
# >>> Cat.objects.all()
# should return a QuerySet

# Step 7.4 CREATING a NEW OBJECT 
# all data must be provided as a KWARG
# >>> c = Cat(
# name="Princess Meatball", 
# breed='Bombay',
# description='Protects our realm against ShadowCat. Packs a mean punch.',
# age = 2
# )

# confirm by entering c in python shell

# Step 7.5 SAVE the NEW OBJECT to DATABASE
# enter c.__dict__ to see the new Object's info
# use save() and check it was assigned an ID
# >>> c.save()
# >>> c.id 

# Step 7.6 CONFIRM the NEW OBJECT is in DB
# >>> Cat.objects.all()
# should return a QuerySet with an object

# Step 7.7 ADD a STR METHOD to MODEL
# changing this INSTANCE METHOD does not impact the DATABASE,
# therefore no makemigrations are necessary

def __str__(self):
    return f'{self.name} ({self.id})'




