from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # Link to the post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # User who wrote the comment
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the creation time
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set the update time

    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
        ]

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.post.pk})

