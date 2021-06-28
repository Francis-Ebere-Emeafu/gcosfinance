from django.urls import path

from assessment.views import (
    questions,
    projects,
)

urlpatterns = [
    path('questions', questions, name="questions"),
    path('projects', projects, name="projects"),
    # path('start', start, name="start"),
    # path('register', register, name="register"),
    #
    # path('<user_id>/edit', edit_account_view, name="edit"),
]
