from django.db import models
from django.db import models
from django.conf import settings
import uuid
from user.models import User

class Deck(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    tags = models.JSONField(default=list, blank=True) 
    is_public = models.BooleanField(default=True)
    rating = models.FloatField(default=0.0)
    rating_count = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    saved_count = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='decks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MCQ(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='mcqs')
    is_multiselect = models.BooleanField(default=False)
    question_text = models.TextField()
    options = models.JSONField(default=list, blank=True) 
    correct_answers = models.JSONField(default=list, blank=True) 
    explanation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text
