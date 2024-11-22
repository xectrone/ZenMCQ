from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DeckForm, MCQForm
from .models import Deck, MCQ
import json

@login_required
def create_deck_view(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.owner = request.user
            deck.save()
            messages.success(request, "Deck created successfully!")
            return redirect('deck_detail', deck_id=deck.id)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = DeckForm()
    return render(request, 'deck/create_deck.html', {'form': form})

@login_required
def add_mcq_view(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, owner=request.user)
    if request.method == 'POST':
        form = MCQForm(request.POST)
        if form.is_valid():
            mcq = form.save(commit=False)
            mcq.deck = deck
            # Handle dynamic fields
            mcq.options = request.POST.getlist('options[]')
            mcq.correct_answers = json.loads(request.POST.get('correct_answers', '[]'))  # Parse the JSON list
            mcq.save()
            messages.success(request, "MCQ added successfully!")
            return redirect('deck_detail', deck_id=deck.id)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = MCQForm()

    return render(request, 'mcq/add_mcq.html', {'form': form, 'deck': deck})


@login_required
def deck_detail_view(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    mcqs = deck.mcqs.all()
    return render(request, 'deck/deck_detail.html', {'deck': deck, 'mcqs': mcqs})

@login_required
def all_decks_view(request):
    decks = Deck.objects.prefetch_related('mcqs').all()  # Fetch decks and their MCQs efficiently
    context = {'decks': decks}
    return render(request, 'deck/all_decks.html', context)