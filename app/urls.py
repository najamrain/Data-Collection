from django.urls import path
from . import views

# app_name = 'app'

urlpatterns = [
    path('', views.homepage, name='home_page'),
    path('companies/', views.company_list, name='company_list'),
    path('company_detail/<int:company_id>/', views.company_detail, name='company_detail'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('photos/', views.photo_list, name='photo_list'),
    path('photos/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('projects_by_company/<int:company_id>/', views.projects_by_company, name='projects_by_company'),
    # path('create_project/', views.create_project, name='create_project'),
    path('create_project/<int:company_id>/', views.create_project, name='create_project'),
    path('upload_photo/<int:company_id>/<int:project_id>/', views.upload_photo, name='upload_photo'),# path('upload_photo/<int:project_id>/', views.upload_photo, name='upload_photo'),
    path('edit_project/<int:pk>/', views.ProjectUpdateView.as_view(), name='edit_project'),
    path('delete_project/<int:pk>/', views.ProjectDeleteView.as_view(), name='delete_project'),
    path('edit_photo/<int:pk>/', views.PhotoUpdateView.as_view(), name='edit_photo'),
    path('delete_photo/<int:pk>/', views.PhotoDeleteView.as_view(), name='delete_photo'),
    ]


