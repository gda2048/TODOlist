from django.urls import path, re_path
from main.views import CardCreateView, CardDeleteView, CardUpdateView, card_return, card_archive, card_list

urlpatterns = [
    path('', card_list, name='card-list'),
    re_path(r'card/add', CardCreateView.as_view(), name='card-add'),
    re_path(r'card/return', card_return, name='card-return'),
    re_path(r'card/archive', card_archive, name='card-archive'),
    re_path(r'card/delete/(?P<pk>\d+)', CardDeleteView.as_view(), name='card-delete'),
    re_path(r'card/update/(?P<pk>\d+)', CardUpdateView.as_view(), name='card-update'),
]
