from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    op = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self) -> str:
        return f'{self.title} | {self.op.username}'

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    body = models.TextField()

    def __str__(self) -> str:
        return f'Answer on {self.question.title}'