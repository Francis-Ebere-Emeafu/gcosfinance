from django.urls import path

from account.views import (
    start,
    register,
)

urlpatterns = [
    path('start', start, name="start"),
    path('register', register, name="register"),

    # path('<user_id>/edit', edit_account_view, name="edit"),
]
