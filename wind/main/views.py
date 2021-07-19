from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, "index.html")

def view_question(req, pk):
    return render(req, 'view_question.html', {'pk': pk})