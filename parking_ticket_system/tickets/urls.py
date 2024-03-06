from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_ticket, name="create_ticket"),
    path("<int:ticket_id>/", views.view_ticket, name="view_ticket"),
    path("list/", views.list_tickets, name="list_tickets"),
]
