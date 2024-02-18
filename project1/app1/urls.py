from . import views
from django.urls import path

urlpatterns = [

    #path('', views.fn1,name='fn1'),
    # path('',views.form,name='form'),
    # path('arith/',views.arithmetics,name='arithmetics'),
    path('',views.travel,name='travel')
]