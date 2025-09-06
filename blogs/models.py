from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()

    def __str__(self):
        return self.comment