from django.urls import path
from . import views
urlpatterns = [
    path('<slug:slug>',views.main_slug.as_view()),
    path('', views.main.as_view(), name='main'),

]