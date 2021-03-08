from django.contrib import admin
from django.urls import path, include
from projects.views import ProjectView, CredentialsListView, DeleteCredentialView

app_name = "projects"

urlpatterns = [

    path('', CredentialsListView.as_view(), name="list_credentials"),
    path('<int:credential_id>/delete/', DeleteCredentialView.as_view(), name="delete_credentials"),
    path('new/', ProjectView.as_view(), name="project"),
]
