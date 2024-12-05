from django.urls import path
from . import views
urlpatterns=[
    path('',views.mob_login),
    path('mob_logout',views.mob_logout),

    #admin
    path('home_ad',views.home_ad),
    path('add_product',views.add_prod),
    path('edit/<pid>',views.edit_product),
    path('delete/<pid>',views.delete_product),
    path('bookings',views.bookings),

    #user
    path('register',views.register),
    path('user_home',views.user_home),
    path('view_pro/<pid>',views.view_pro),
    # path('user_products',views.user_products),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart',views.view_cart),
    path('delete_cart/<id>',views.delete_cart),
    path('user_buy/<cid>',views.user_buy),
    path('user_buy1/<pid>',views.user_buy1),
    path('user_bookings',views.user_bookings)
]