from django.contrib import admin
from .models import Question, Answer

# Register your models here.

admin.site.register(model_or_iterable=Question)
admin.site.register(Answer)