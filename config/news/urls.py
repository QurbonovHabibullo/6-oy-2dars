from django.urls import path
from .views import home,about,contact,view4,view5,view6,view7,view8,view9,view10

urlpatterns = [
    path('',home, name='home'),  # Home sahifasi
    path('about/',about, name='about'),  # About sahifasi
    path('contact/',contact,name='contact'),  # Contact sahifasi
    path('view4/', view4,name='view4'),
    path('view5/', view5,name='view5'),
    path('view6/', view6,name='view6'),
    path('view7/', view7,name='view7'),
    path('view8/', view8,name='view8'),
    path('view9/', view9,name='view9'),
    path('view10/',view10,name='view10'),
]
