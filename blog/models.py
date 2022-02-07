from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'\nTitle:{self.title}\n'

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk': self.pk})    
