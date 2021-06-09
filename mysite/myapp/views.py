from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

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

@login_required
def comment_view(request, sugg_id):
    if not request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form_instance = forms.CommentForm(request.POST)
        if form_instance.is_valid():
            form_instance.save(request, sugg_id)
            return redirect("/")
    else:
        form_instance = forms.CommentForm()
    context = {
        "title":"Comment",
        "form":form_instance,
        "sugg_id": sugg_id,
    }
    return render(request, "comment.html", context=context)

@login_required
def suggestion_view(request):
    if not request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form_instance = forms.SuggestionForm(request.POST)
        if form_instance.is_valid():
            form_instance.save(request)
            return redirect("/")
    else:
        form_instance = forms.SuggestionForm()
    context = {
        "title":"Suggestion",
        "form":form_instance
    }
    return render(request, "suggestion.html", context=context)

def suggestions_view(request):
    suggestion_objects = models.SuggestionModel.objects.all()

    suggestion_list = {}
    suggestion_list["suggestions"]=[]
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
        suggestion_list["suggestions"].append(temp_sugg)
    return JsonResponse(suggestion_list)