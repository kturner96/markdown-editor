from django.urls import path

from . import views

urlpatterns = [
    path('', views.editor, name="editor_new"),
    path('<int:pk>/', views.editor, name="editor")
]
