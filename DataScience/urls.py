from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('handle_uploaded_file/', views.handle_uploaded_file, name='handle_uploaded_file'),
    path('data_cleaning/', views.data_cleaning, name='data_cleaning'),
    path('data_visualization/', views.data_visualization, name='data_visualization'),
    path('visualize_selected_combinations/', views.visualize_selected_combinations, name='visualize_selected_combinations'),
    path('reload_data/', views.reload_data, name='reload_data'),
    path('perform_operation/', views.perform_operation, name='perform_operation'),
    #path('display_combination_visualization/', views.display_combination_visualization, name='display_combination_visualization'),
   

]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)