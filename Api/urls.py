

from django.urls import path
from .import views
urlpatterns = [

    path('',views.home),
    path('skils-api/',views.skilApi.as_view(),name="skill"),
    path('project-model-api/',views.projectModelApi.as_view(),name="project"),
]