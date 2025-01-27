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

    path('list/', views.list_categories, name='list_categories'), 
    path('new/', views.new_category, name='new_category'),  
    path('save/', views.save_category, name='save_category'),  
    path('edit/<int:id>/', views.edit_category, name='edit_category'),  
    path('update/<int:id>/', views.update_category, name='update_category'),  
    path('delete/<int:id>/', views.delete_category, name='delete_category'),

    path('list/', views.list_tags, name='list_tags'),  
    path('new/', views.new_tag, name='new_tag'),  
    path('save/', views.save_tag, name='save_tag'),  
    path('edit/<int:id>/', views.edit_tag, name='edit_tag'),  
    path('update/<int:id>/', views.update_tag, name='update_tag'),  
    path('delete/<int:id>/', views.delete_tag, name='delete_tag'),

    path('list/', views.list_projects, name='list_projects'),  
    path('new/', views.new_project, name='new_project'),  
    path('save/', views.save_project, name='save_project'),  
    path('edit/<int:id>/', views.edit_project, name='edit_project'),  
    path('update/<int:id>/', views.update_project, name='update_project'), 
    path('delete/<int:id>/', views.delete_project, name='delete_project'),
]