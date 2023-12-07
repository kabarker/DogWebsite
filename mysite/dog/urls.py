from . import views
from django.urls import path
from django.conf.urls.static import static

app_name = 'dog'

urlpatterns = [
    path('about/', views.about, name="about"),
    path('faq/', views.faq, name="faq"),
    path('rental/', views.rental, name="rental"),

    path('contact/', views.contact, name="contact"),
    path('contact_list/', views.contact_list, name="contact_list"),
    path('contact/delete/<int:id>', views.delete_contact, name="delete_contact"),

    path('trainers/', views.trainers, name="trainers"),
    path('trainer/add', views.create_trainer, name="create_trainer"),
    path('trainer/update/<int:id>', views.trainer_update, name="update_trainer"),
    path('trainer/delete/<int:id>', views.trainer_delete, name="delete_trainer"),

    path('products/', views.products, name="products"),
    path('product/delete/<int:id>', views.delete_product, name="delete_product"),
    path('product/add', views.create_product, name="create_product"),
    path('product/update/<int:id>', views.product_update, name="update_product"),

    path('agilityclasses/', views.agilityclasses, name="agilityclasses"),
    path('agilityclasses/add', views.create_agilityclasses, name="create_agilityclasses"),
    path('agilityclasses/update/<int:id>', views.agilityclasses_update, name="update_agilityclasses"),
    path('agilityclasses/delete/<int:id>', views.delete_agilityclasses, name="delete_agilityclasses"),
    path('agilityclasses/details/<int:id>', views.agility_detail, name="agility_detail"),

    path('obedienceclasses/', views.obedienceclasses, name="obedienceclasses"),
    path('obedienceclasses/add', views.create_obedienceclasses, name="create_obedienceclasses"),
    path('obedienceclasses/<int:id>', views.obedience_detail, name="obedience_detail"),
    path('obedienceclasses/delete/<int:id>', views.delete_obedienceclasses, name="delete_obedienceclasses"),
    path('obedienceclasses/update/<int:id>', views.obedienceclasses_update, name="update_obedienceclasses"),
]