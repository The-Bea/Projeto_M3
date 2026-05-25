from django.urls import path
from .views import home_view, post_detail_view, async_view 

urlpatterns = [
    path('', home_view, name='home'),
    path('post/<int:pk>/', post_detail_view, name='post_detail'),
    path('async/', async_view, name='async_view'),
]