from django.urls import path
from . import view


urlpatterns = [
    path('create',view.create),
    path('update',view.update),
    path('delete',view.delete),
    path('retreive',view.retrieve),
    path('list',view.listAll)
]


