from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question posted by {self.created_by}"
    
class Answer(models.Model):
    answer_text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="answer_likes", symmetrical=False, blank=True)
    
    def __str__(self):
        return f''' "{self.created_by}" answered to {self.question.created_by}'s question '''
