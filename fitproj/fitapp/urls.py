from django.urls import path
from fitapp import views

app_name = 'fitapp'

urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),

]
