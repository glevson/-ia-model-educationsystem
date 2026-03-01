from django.urls import path
from .views import index, PredictAPI

urlpatterns = [
    path('', index, name='index'),
    path('api/predict/', PredictAPI.as_view(), name='predict_api'),
]