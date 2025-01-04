from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-models/', views.get_models, name='get_models'),
    path('fetch-data/', views.fetch_data, name='fetch_data'),
    path('trend-analysis/', views.trend_analysis, name='trend_analysis'),
    path('scraping/', views.scraping, name='scraping'),
    
]
