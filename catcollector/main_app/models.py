from django.db import models
# VID 3 (CBVs) Part 5 Step 5.7
# import REVERSE
from django.urls import reverse

# Create your models here.

# VID 4 (One to Many) Step 3.2
# CREATE the MEALS MODEL as TUPLE of TWO TUPLES (one to many model)
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


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

# Step 7.2 (C - CREATE) IMPORT model to DB
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

# Step 7.8 RELOAD the SHELL
# use exit() or crtl+D to leave the shell
# relaunch the shell using python3 manage.py shell
# RE-IMPORT your MODEL
# from main_app.models import Cat

# Step 7.9 (U - UPDATE) UPDATE an OBJECT

# to view the FIRST ROW of your DB use first()
# to view the LAST ROW of your DB use last()
# SELECT the attribute using first() or last()
# then OVERRIDE the VALUE you want using dot notation
# then SAVE it using save()
# (Example)
# >>> c = Cat.objects.first()
# >>> c
#  <Cat: Princess Meatball>
# >>> c.name = 'Meatball'
# >>> c.save()
# >>> c
# <Cat: Meatball>

# Step 7.10 FILTERING / QUERING for RECORDS objects.filter()
# these kinds of queries are called FIELD LOOKUPS
# >>> Cat.objects.filter(name="Meatball")
# <QuerySet [<Cat: Meatball>]>

# you can use contains, gte and lte to filter search
# >>> Cat.objects.filter(name_contains='Meat')
# >>> Cat.objects.filter(age_lte=5)

# Step 7.11 RETURN A SINGLE RECORD / SINGLE OBJECT get()
# use GET METHOD and provide an ID #
# >>> Cat.objects.get(id=1)

# Step 7.12 ORDERING OBJECTS (SHORTING) order_by('')
# use the ORDER BY METHOD
# >>> Cat.objects.order_by('age')

# for DESCENDING ORDER use a negative sign before string
# Cat.objects.order_by('-age')

# it can be INDEXED too if you need
# >>> Cat.objects.order_by('-age')[0]


# #############################

# VID 3 (CBVs) Part 5 Step 5.6
# ADD an INSTANCE METHOD for an ABSOLUTE URL
def get_absolute_url(self):
    # use return REVERSE to return the correct path for DETAIL named route
    return reverse('detail', kawrgs={'cat_id': self.id})

# #############################
# VID 4 (One To Many)

# Part 3.1 ADD the FEEDING MODEL as a new CLASS
# ORDER does matter here so be sure to add new models below the main model

class Feeding(models.Model):
    # Step 7.3 add CUSTOM FIELD LABEL to DateField
    date = models.DateField('feeding Date')
    meal = models.CharField(
        max_length=1,
        # Step 3.3 use CHOICES to add FIELD OPTION
        choices=MEALS,
        # now set a default choice
        default=MEALS[0][0]
    )
    # ^^^ using max_length=1 ONLY to show how STRINGS 
    # with only ONE CHARACTER can be FIELD CHOICES

# Part 3.5 CREATE a FOREIGN KEY of cat for cat_id
    cat = models.ForeignKey(
        Cat, 
        on_delete=models.CASCADE
    )

# Part 3.4 ADD the __STR__ METHOD to FEEDING CLASS OBJECT
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    # VID 5 (One to Many) -- ORDERING your FEEDINGS w NESTED CLASS
    class Meta:
        ordering = ['-date']

# Part 5 MAKE MIGRATIONS to DATABASE'S SCHEMA
# python3 manage.py makemigrations
# python3 manage.py showmigrations
# python3 manage.py migrate

# Part 6 TEST the MODELS in the SHELL
# python3 manage.py shell

# Part 6.1 IMPORT the MODEL
# use * to import EVERYTHING instead of individual features
# >>> from main_app.models import *
# >>> Feeding
# <class 'main_app.models.Feeding'>
# >>> MEALS
# (('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner'))

# Paet 6.2 CREATE A FEEDING for a CAT (One to Many) in SHELL ORM

# get first cat object in db [√]
# >>> c = Cat.objects.first()   # or Cat.objects.all()[0]
# >>> c
# <Cat: Maki>

# obtain all feeding objects for a cat using the "related manager" object [√]
# >>> c.feeding_set.all()
# <QuerySet []>

# create a feeding for a given cat [√]
# >>> c.feeding_set.create(date='2022-10-06')
# <Feeding: Breakfast on 2022-10-06>

# yup, it's there and the default of 'B' for the meal worked [√]
# >>> Feeding.objects.all()
# <QuerySet [<Feeding: Breakfast on 2022-10-06>]>

# and it belongs to a cat [√]
# >>> c.feeding_set.all()
# <QuerySet [<Feeding: Breakfast on 2022-10-06>]>

# get the first feeding object in the db [√]
# >>> f = Feeding.objects.first()
# >>> f
# <Feeding: Breakfast on 2022-10-06>

# cat is the name of the field we defined in the Feeding model [√]
# >>> f.cat
# <Cat: Maki>
# >>> f.cat.description
'Lazy but ornery & cute'

# another way to create a feeding for a cat [√]
# >>> f = Feeding(date='2022-10-06', meal='L', cat=c)
# >>> f.save()
# >>> f
# <Feeding: Lunch on 2022-10-06>
# >>> c.feeding_set.all()
# <QuerySet [<Feeding: Breakfast on 2022-10-06>, <Feeding: Lunch on 2022-10-06>]>

# finish the day's feeding, this time using the create method [√]
# >>> Feeding.objects.create(date='2022-10-06', meal='D', cat=c)
# >>> c.feeding_set.count()
# 3

# feed another cat
# (ensure a cat with id of 3 exists)
# >>> c = Cat.objects.get(id=3)
# >>> c
# <Cat: Whiskers>
# >>> c.feeding_set.create(date='2022-10-07', meal='B')
# <Feeding: Breakfast on 2022-10-07>
# >>> Feeding.objects.filter(meal='B')
# <QuerySet [<Feeding: Breakfast on 2022-10-06>, <Feeding: Breakfast on 2022-10-07>]>

# the foreign key (cat_id) can be used as well
# >>> Feeding.objects.filter(cat_id=2)
# <QuerySet [<Feeding: Breakfast on 2022-10-06>, <Feeding: Lunch on 2022-10-06>, <Feeding: Dinner on 2022-10-06>]>
# >>> Feeding.objects.create(date='2022-10-07', meal='L', cat_id=3)
# >>> Cat.objects.get(id=3).feeding_set.all()
# <QuerySet [<Feeding: Breakfast on 2022-10-07>, <Feeding: Lunch on 2022-10-07>]>
# exit()
