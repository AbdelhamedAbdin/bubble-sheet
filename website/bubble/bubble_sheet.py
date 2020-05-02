from .models import Answer


def all_answers():
    for answers in Answer.objects.all():
        choose = ((answers.answer),(answers.answer),)
        return choose
