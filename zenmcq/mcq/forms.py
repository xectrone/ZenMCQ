from django import forms
from .models import Deck, MCQ

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['name', 'description', 'tags', 'is_public']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Deck Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Deck Description', 'rows': 4}),
            'tags': forms.TextInput(attrs={'placeholder': 'Comma-separated tags (max 5)'}),
        }

class MCQForm(forms.ModelForm):
    class Meta:
        model = MCQ
        fields = ['question_text', 'is_multiselect', 'options', 'correct_answers', 'explanation']
        widgets = {
            'question_text': forms.Textarea(attrs={'placeholder': 'Enter the question', 'rows': 3}),
            'options': forms.TextInput(attrs={'placeholder': 'Comma-separated options'}),
            'correct_answers': forms.TextInput(attrs={'placeholder': 'Comma-separated indices of correct options'}),
            'explanation': forms.Textarea(attrs={'placeholder': 'Optional explanation', 'rows': 2}),
        }
