from django.urls import path
from . import views

urlpatterns = [
    # path('monday/', views.monday),
    # path('tuesday/', views.tuesday),
    path("<int:day_of_week>/", views.what_to_do_by_number),
    path("<str:day_of_week>/", views.what_to_do, name='day-number'),
    ]
