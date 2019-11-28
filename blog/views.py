from django.http import HttpResponse
from django.shortcuts import render
from block import models

def index(request):
    #return HttpResponse("Hello World")
    #read index.html content as data from index.html,and then return HttpResponse(data)
    #block_infos = models.Block.objects.all().order_by("id")
    block_infos = models.Block.objects.filter(status=0).order_by("-id")

    return render(request,"index.html",{"blocks":block_infos})
