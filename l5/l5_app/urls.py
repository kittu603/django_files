from django.urls import path,include
from l5_app import views

app_name = 'l5_app'


urlpatterns = [
    path('register/', views.register,name='register'),
    path('',views.index,name='index'),
    path('user_login/',views.user_login,name='user_login')

]
