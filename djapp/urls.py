from django.urls import path
from  . import views

urlpatterns = [
    path('home/', views.home ,name = "home"),
    path('main/',views.main, name ='main'),
    path('detail/<std_id>' , views.std_detail , name ='detail'),
    path('delete/<std_id>', views.delete , name = 'delete'),
    path('add/', views.add , name = 'add'),
    path('edit/<std_id>', views.edit , name = 'edit'),
    path('cv/', views.cv , name = 'cv'),
# rest
    path('api/', views.api , name = 'api'),
    path('api/<std_id>', views.api_one , name = 'api_one'),
    path('api_add/', views.api_add , name = 'api_add'),
    path('api_edit/<std_id>', views.api_edit , name = 'api_edit'),
    path('api_del/<std_id>', views.api_del , name = 'api_del'),
    

]
