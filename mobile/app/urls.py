from django.urls import path
from . import views
urlpatterns=[
    path('',views.mob_login),
    path('mob_logout',views.mob_logout),

    #admin
    path('home_ad',views.home_ad),
    path('add_product',views.add_product),
    path('edit/<pid>',views.edit_product),
    path('delete/<pid>',views.delete_product),

    #user
    path('register',views.register),
    path('user_home',views.user_home),
    path('view_pro/<pid>',views.view_pro),
]