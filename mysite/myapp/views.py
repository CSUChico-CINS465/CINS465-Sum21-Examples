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
    suggestion_objects = models.SuggestionModel.objects.all()

    suggestion_list = []
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(
            suggestion=sugg
        )
        temp_sugg = {}
        temp_sugg["suggestion"] = sugg.suggestion
        temp_sugg["id"] = sugg.id
        temp_sugg["author"] = sugg.author.username
        temp_sugg["comments"] = []
        for comm in comment_objects:
            temp_comm = {}
            temp_comm["comment"] = comm.comment
            temp_comm["author"] = comm.author.username
            temp_comm["id"] = comm.id
            temp_sugg["comments"] += [temp_comm]
        suggestion_list.append(temp_sugg)

    context = {
        "title": "CINS 465",
        "body": "Body",
        "list": suggestion_list,
        "form": suggestion_form
    }
    return render(request, "index.html", context=context)
