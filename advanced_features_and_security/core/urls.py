from LibraryProject.relationship_app import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('LibraryProject.relationship_app.urls')),  # All authentication URLs will be prefixed with 'auth/'
    
    path('', views.home, name='Home'),

]
