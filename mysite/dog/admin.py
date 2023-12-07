from django.contrib import admin
from .models import AgilityClass
from .models import Product
from .models import NonAgilityClass
from .models import Trainer
from .models import Contact

# Register your models here.
admin.site.register(AgilityClass)
admin.site.register(NonAgilityClass)
admin.site.register(Product)
admin.site.register(Trainer)
admin.site.register(Contact)
