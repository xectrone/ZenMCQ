from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    last_name = models.CharField(max_length=150, blank=True, null=True)
    REQUIRED_FIELDS = [ 'first_name', 'email']
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    interests = models.JSONField(default=list, blank=True)  # List of tags (up to 5)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username