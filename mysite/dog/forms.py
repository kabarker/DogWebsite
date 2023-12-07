from django import forms
from .models import Trainer
from .models import AgilityClass
from .models import NonAgilityClass
from .models import Product
from .models import Contact

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['trainer_name', 'trainer_description', 'trainer_image']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'product_price', 'product_image' ]

class AgilityForm(forms.ModelForm):
    class Meta:
        model = AgilityClass
        fields = ['agilityclass_name', 'agilityclass_description', 'agilityclass_price', 'agilityclass_length', 'agilityclass_week1',
                  'agilityclass_image', 'agilityclass_week2', 'agilityclass_week3', 'agilityclass_week4', 'agilityclass_week5', 'agilityclass_week6']

class NonAgilityForm(forms.ModelForm):
    class Meta:
        model = NonAgilityClass
        fields = ['nonagilityclass_name', 'nonagilityclass_description', 'nonagilityclass_price', 'nonagilityclass_length',
                   'nonagilityclass_week1','nonagilityclass_image']
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_email', 'contact_message' ]