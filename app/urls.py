from django.urls import path
from .views import main, create, redirect_clicks, delete

urlpatterns = [
    path('', main),
    path('create/', create),
    path('delete/', delete),
    path('<str:url_hash>/', redirect_clicks, name='redirect_clicks'),
]
