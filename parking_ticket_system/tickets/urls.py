from django.urls import path
from . import views

urlpatterns = [
    path(route="create/", view=views.create_ticket, name="create_ticket"),
    path(route="<int:ticket_id>/", view=views.view_ticket, name="view_ticket"),
    path(route="list/", view=views.list_tickets, name="list_tickets"),
]
