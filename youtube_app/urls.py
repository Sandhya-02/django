from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.homefun),
    path('contact/',views.contactfun),
    path('lehanga/',views.lehangafun),
    path('hoodies/',views.hoodiesfun),
]