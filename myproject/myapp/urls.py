from django.urls import path
from .views import submit_view
from . import views 

urlpatterns = [
    path('main/', views.main),
    path('main/submit_form.html', submit_view, name='submit'),
]