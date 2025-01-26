from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),

    path('list/', views.list_technologies, name='list_technologies'),
    path('new/', views.new_technology, name='new_technology'),
    path('save/', views.save_technology, name='save_technology'),
    path('edit/<int:id>/', views.edit_technology, name='edit_technology'),
    path('update/<int:id>/', views.update_technology, name='update_technology'),
    path('delete/<int:id>/', views.delete_technology, name='delete_technology'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)