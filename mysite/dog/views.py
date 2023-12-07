from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Trainer
from .models import Product
from .models import AgilityClass
from .models import NonAgilityClass
from .models import Contact

from django.template import loader
import io

from .forms import TrainerForm
from .forms import AgilityForm
from .forms import NonAgilityForm
from .forms import ProductForm
from .forms import ContactForm


# Create your views here.
#already have data
def about(request):
    context ={}
    return render(request,'dog/about.html', context)

def rental(request):
    context ={}
    return render(request,'dog/rental.html', context)

def faq(request):
    context ={}
    return render(request,'dog/faq.html', context)



#pull from database
def trainers(request):
    trainers_list = Trainer.objects.all() 
    context = {
        'trainers_list':  trainers_list,
    }
    return render(request,'dog/trainers.html', context)

def products(request):
    products_list = Product.objects.all()
    context = {
        'products_list':  products_list,
    }
    return render(request,'dog/products.html', context)

def agilityclasses(request):
    agilityclass_list = AgilityClass.objects.all()
    context = {
        'agilityclass_list':  agilityclass_list,
    }
    return render(request,'dog/agilityclasses.html', context)

def obedienceclasses(request):
    obedienceclass_list = NonAgilityClass.objects.all()
    context = {
        'obedienceclass_list':  obedienceclass_list,
    }
    return render(request,'dog/obedienceclasses.html', context)

def contact_list(request):
    contacts_list = Contact.objects.all()
    context = {
        'contacts_list':  contacts_list,
    }
    return render(request,'dog/contact_list.html', context)


#delete items
def trainer_delete(request, id):
    trainer = Trainer.objects.get(id=id)
    context = {
        'trainer': trainer
    }

    if request.method == 'POST':
        trainer.delete()
        return redirect('dog:trainers')
    
    return render(request, 'dog/trainer_delete.html', context)


def delete_agilityclasses(request, id):
    agilityclass = AgilityClass.objects.get(id=id)
    context = {
        'agilityclass': agilityclass
    }

    if request.method == 'POST':
        agilityclass.delete()
        return redirect('dog:agilityclasses')
    
    return render(request, 'dog/agilityclass_delete.html', context)

def delete_obedienceclasses(request, id):
    obedienceclass = NonAgilityClass.objects.get(id=id)
    context = {
        'obedienceclass': obedienceclass
    }

    if request.method == 'POST':
        obedienceclass.delete()
        return redirect('dog:obedienceclasses')
    
    return render(request, 'dog/obedienceclass_delete.html', context)

def delete_product(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }

    if request.method == 'POST':
        product.delete()
        return redirect('dog:products')
    
    return render(request, 'dog/product_delete.html', context)



#update items
def trainer_update(request,id):
    trainer = Trainer.objects.get(pk=id)
    form = TrainerForm(request.POST or None, instance=trainer)

    if form.is_valid():
        form.save()
        return redirect('dog:trainers')
    
    return render(request, 'dog/trainer-form.html', {'form': form, 'trainer': trainer})

def product_update(request,id):
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('dog:products')
    
    return render(request, 'dog/product-form.html', {'form': form, 'product': product})

def agilityclasses_update(request,id):
    agilityclass = AgilityClass.objects.get(pk=id)
    form = AgilityForm(request.POST or None, instance=agilityclass)

    if form.is_valid():
        form.save()
        return redirect('dog:agilityclasses')
    
    return render(request, 'dog/agilityclass-form.html', {'form': form, 'agilityclass': agilityclass})

def obedienceclasses_update(request,id):
    obedienceclass = NonAgilityClass.objects.get(pk=id)
    form = NonAgilityForm(request.POST or None, instance=obedienceclass)

    if form.is_valid():
        form.save()
        return redirect('dog:obedienceclasses')
    
    return render(request, 'dog/obedienceclass-form.html', {'form': form, 'obedienceclass': obedienceclass})


#add items
def create_trainer(request):
    form = TrainerForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dog:trainers')
    
    return render(request, 'dog/trainer-form.html', {'form': form})

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dog:products')
    
    return render(request, 'dog/product-form.html', {'form': form})

def create_agilityclasses(request):
    form = AgilityForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dog:agilityclasses')
    
    return render(request, 'dog/agilityclass-form.html', {'form': form})

def create_obedienceclasses(request):
    form = NonAgilityForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dog:obedienceclasses')
    
    return render(request, 'dog/obedienceclass-form.html', {'form': form})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('dog:about')
        
    return render(request, 'dog/contact.html', {'form': form})


#detail pages

def agility_detail(request, id):
    agility = AgilityClass.objects.get(pk=id)
    context ={
        'agility':agility
    }

    return render(request,'dog/agilityclass_detail.html', context)


def obedience_detail(request, id):
    classes = NonAgilityClass.objects.get(pk=id)
    context ={
        'classes':classes
    }

    return render(request,'dog/obedienceclass_detail.html', context)


##delete contact
def delete_contact(request,id):
    contact = Contact.objects.get(id=id)

    context = {
            'contact': contact
        }

    if request.method == 'POST':
        contact.delete()
        return redirect('dog:contact_list')
    
    return render(request, 'dog/contact_delete.html', context)

##pdf download
