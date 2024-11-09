from django.contrib import admin
#from .models import related models
from django.contrib import admin
from .models import CarMake, CarModel

# Registering the models to make them available in the admin interface
admin.site.register(CarMake)
admin.site.register(CarModel)


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
