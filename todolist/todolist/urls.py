from django.urls import path
from main.views import card_list, CardCreateView, card_return, card_archive

urlpatterns = [
    path('', card_list, name='card-list'),
    path('card/add', CardCreateView.as_view(), name='card-add'),
    path('card/return', card_return, name='card-return'),
    path('card/archive', card_archive, name='card-archive'),
]
