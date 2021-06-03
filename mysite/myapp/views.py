from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, page=0):
    content = list(range(page*10,page*10+10,1))
    context = {
        "title":"CINS 465",
        "body":"Body",
        "list":content,
        "next":page+1,
        "prev":page-1
    }
    return render(request,"index.html",context=context)