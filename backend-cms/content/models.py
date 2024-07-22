from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    template = models.CharField(max_length=50, choices=[
        ('template1', 'Template 1'),
        ('template2', 'Template 2'), 
    ], default='template1')

    def __str__(self):
        return self.title
