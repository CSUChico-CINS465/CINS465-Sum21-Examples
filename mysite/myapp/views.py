from django.shortcuts import render, redirect
from django.contrib.auth import logout, login

from . import models
from . import forms

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('/login/')


def index(request):
    if request.method == "POST":
        suggestion_form = forms.SuggestionForm(request.POST)
        if request.user.is_authenticated:
            if suggestion_form.is_valid():
                suggestion_form.save(request)
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

def register_view(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            user = form_instance.save()
            # login(request, user)
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()

    context = {
        "title":"Registration",
        "form":form_instance
    }

    return render(request, "registration/register.html", context=context)
