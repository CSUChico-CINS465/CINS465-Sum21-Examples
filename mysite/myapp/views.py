from django.shortcuts import render

from . import models
from . import forms

# Create your views here.
def index(request):
    if request.method == "POST":
        suggestion_form = forms.SuggestionForm(request.POST)
        if suggestion_form.is_valid():
            suggestion_form.save() 
            suggestion_form = forms.SuggestionForm()
    else:
        suggestion_form = forms.SuggestionForm()
    content = models.SuggestionModel.objects.all()
    
    context = {
        "title":"CINS 465",
        "body":"Body",
        "list":content,
        "form":suggestion_form
    }
    return render(request,"index.html",context=context)