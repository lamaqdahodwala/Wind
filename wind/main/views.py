from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html')

def question(req, pk):
    return render(req, 'question.html', {'props': {'pk': pk}})