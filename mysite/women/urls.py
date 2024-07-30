from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.ForDigitYearConverter, "year4")

urlpatterns = [
    # 127.0.01:8000/
    path('', views.index, name='home'),                                                             
    # 127.0.01:8000/cats/id/
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),    
    # 127.0.01:8000/cats/slug/
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),  
    # 127.0.01:8000/archive/1992/
    path('archive/<year4:year>/', views.archive, name='archive'),

]