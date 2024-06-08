from django.urls import path
from  . import views

urlpatterns = [
    path('home/', views.home ,name = "home"),
    path('main/',views.main, name ='main'),
    path('detail/<std_id>' , views.std_detail , name ='detail'),
    path('delete/<std_id>', views.delete , name = 'delete'),

]
