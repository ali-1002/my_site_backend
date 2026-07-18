from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.name
