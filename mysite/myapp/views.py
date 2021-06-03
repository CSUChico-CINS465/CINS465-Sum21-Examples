from django.shortcuts import render

from . import models

# Create your views here.
def index(request):
    content = models.SuggestionModel.objects.all()
    print(content)
    context = {
        "title":"CINS 465",
        "body":"Body",
        "list":content,
    }
    return render(request,"index.html",context=context)