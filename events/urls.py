from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('<int:event_id>/', views.event_listing, name='event_listing'),
    path('add/', views.add_event, name='add_event'),
    path('edit/<int:event_id>', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>', views.delete_event, name='delete_event'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('edit_blog/<post_id>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<post_id>/', views.delete_blog, name='delete_blog'),
]
