from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250)
    color = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    url = models.URLField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='videos', blank=True, null=True)
    
    def __str__(self):
        return self.title


