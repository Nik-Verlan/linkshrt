from django.urls import path
from .views import main, create, redirect_clicks, delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main),
    path('create/', create),
    path('delete/', delete),
    path('<str:url_hash>/', redirect_clicks, name='redirect_clicks'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
