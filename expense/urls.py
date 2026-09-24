from django.urls import path
from .import views
from django.contrib import admin

urlpatterns=[
    
    # path('admin/',admin.site.urls)
    # path('admin/',admin.site.urls)
    # path('admin/',admin.site.urls)
    path('home/',views.home,name='home'),
    path('insert/',views.insert,name='insert'),
    path('show/',views.show,name='show'),
    path('search/',views.search,name='search'),
    path('update/<int:id>/',views.update,name='update'),
    path('updated/<int:id>/',views.updated,name='updated'),
    path('delete/<int:id>/',views.delete,name='delete')
]