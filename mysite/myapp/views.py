from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

from datetime import datetime, timezone

from . import models
from . import forms

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('/login/')


def index(request):
    context = {
        "title": "CINS 465",
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
        form_instance = forms.SuggestionForm(request.POST, request.FILES)
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
    suggestion_objects = models.SuggestionModel.objects.all().order_by('-published_on')

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
        temp_sugg["date"] = sugg.published_on.strftime("%Y-%m-%d")
        if sugg.image:
            temp_sugg["image"] = sugg.image.url
            temp_sugg["image_desc"] = sugg.image_description
        else:
            temp_sugg["image"] = ""
            temp_sugg["image_desc"] = ""
        temp_sugg["comments"] = []
        for comm in comment_objects:
            temp_comm = {}
            temp_comm["comment"] = comm.comment
            temp_comm["author"] = comm.author.username
            temp_comm["id"] = comm.id
            time_diff = datetime.now(timezone.utc) - comm.published_on
            time_diff_s = time_diff.total_seconds()
            if time_diff_s < 60:
                temp_comm["date"] = "published " + str(int(time_diff_s)) + " seconds ago"
            else:
                time_diff_m = divmod(time_diff_s, 60)[0]
                if time_diff_m < 60:
                    temp_comm["date"] = "published " + str(int(time_diff_m)) + " minutes ago"
                else:
                    time_diff_h = divmod(time_diff_m, 60)[0]
                    if time_diff_h < 24:
                        temp_comm["date"] = "published " + str(int(time_diff_h)) + " hours ago"
                    else:
                        temp_comm["date"]  = "published on " + comm.published_on.strftime("%Y-%m-%d %H:%M:%S")
            temp_sugg["comments"] += [temp_comm]
        suggestion_list["suggestions"].append(temp_sugg)
    return JsonResponse(suggestion_list)