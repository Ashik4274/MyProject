from django.urls import path
from . import views


app_name = "CrimeReportingSystem"


urlpatterns = [
    path('crimelist', views.Crimes, name='crimelist'),
    path('add', views.Add_create_view, name='add'),
    path('<int:crime_id>/', views.Detail, name='detail-page'),
    path('homepage', views.homepage, name='homepage'),
]
