from django.db import models
from accounts.models import Account

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=5000, blank=True, null=True)
    location = models.CharField(max_length=500)
    contact = models.CharField(max_length=50)
    image = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostComment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(Account, related_name='commments', on_delete=models.CASCADE)
    content = models.TextField(max_length=3000)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ', ' + self.post.title[:40]

