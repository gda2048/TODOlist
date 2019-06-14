from django.views.generic.edit import CreateView
from .models import Card
from django.shortcuts import render, redirect


class CardCreateView(CreateView):
    model = Card
    template_name = 'card_add.html'
    fields = ['name', 'description']
    success_url = '/'


def card_list(request):
    card_ls = Card.objects.filter(is_archived=False)
    card_ls_arch = Card.objects.filter(is_archived=True)
    return render(request, 'cards.html', {"list": card_ls, "list_arch": card_ls_arch})


def card_return(request):
    if request.method == 'POST':
        print(request.POST.getlist('checks'))
        Card.objects.filter(id__in=[int(i) for i in request.POST.getlist('checks')]).update(is_archived=False)
    return redirect("/")


def card_archive(request):
    if request.method == 'POST':
        print(request.POST.getlist('checks'))
        Card.objects.filter(id__in=[int(i) for i in request.POST.getlist('checks') ]).update(is_archived=True)
    return redirect("/")