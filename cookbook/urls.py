from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),   
    url(r'^recipe/(?P<recipe_name_slug>[\w\-]+)/$', views.recipe, name='recipe'),
    url(r'^list$', views.recipe_list, name='recipe_list')
]