from django.urls import path

from main import views

urlpatterns = [
    path('main/', views.index),
    path('<int:pk>', views.ImprisonedView.as_view(), name="imprisoned_detail")
]