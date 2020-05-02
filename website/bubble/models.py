from django.db import models
from .bubble_sheet import all_answers


class Question(models.Model):
    question = models.TextField(max_length=255)
    answer = models.CharField(max_length=150, choices=all_answers(), null=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="questions")
    answer = models.CharField(max_length=150)
