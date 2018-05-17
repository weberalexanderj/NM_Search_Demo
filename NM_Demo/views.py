from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from NM_Demo.forms import CardDisplayForm

import mtgsdk
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog


def CardListView(request, pk):
    if request.method == "POST":
        form = CardDisplayForm(request.POST)
        if form.is_valid():
            keywords = form.cards
            return HttpResponseRedirect(reverse('/'))
    else:
        form = CardDisplayForm()

    return render(request, "index.html", )


def index(request):
    # if request.method == "POST":
    search_term = request.GET.get('keywords')
    search_filter = request.GET.get('searchFilter')

    print("Search type: " + search_filter)

    if search_filter == 'Type':
        cards = Card.where(subtypes=search_term).all()
    elif search_filter == 'Set':
        cards = Card.where(set_name=search_term).all()
    else:
        cards = Card.where(name=search_term).all()

    card_query = cards
    form = CardDisplayForm()
    context = {'cards': card_query, 'form': form }
    if search_term is None:
        context = {}
    return render(request, 'index.html', context)



