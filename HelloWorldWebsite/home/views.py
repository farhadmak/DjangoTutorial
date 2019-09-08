# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from .models import Counter
from django.db import models
import sqlite3
from .nearest import nearest

# Create your views here.
class Home(generic.DetailView):
    # longitude = models.IntegerField()
    # latitude = models.IntegerField()
    # template_name = "home/index.html"
    #
    # treeInfo = models.ListCharField(
    #     base_field = models.CharField(max_length = 30),
    #     size = 18,
    #     max_length = (18 * 31)
    # )
    template_name = "home/index.html"
    def get(self, request, *args, **kwargs):
        # context = {'lat' : }
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        lat_lon_dict = (json.loads(request.body))
        latitude = float(lat_lon_dict["lat"])
        longitude = float(lat_lon_dict["lon"])
        # mydb = sqlite3.connect('../../tree_database.db')
        # mycursor = mydb.cursor()
        treeInfo = nearest(latitude, longitude)
        context = {"nearest_tree": str(treeInfo), "lat":str(treeInfo[15]), "lon":str(treeInfo[16])}


        # return redirect('homepage')
        return HttpResponse(json.dumps(context))
# class Home(generic.DetailView):
#     model = Counter
#     template_name = "home/index.html"

#     def get(self, request, *args, **kwargs):
#         context = {'our_counter' : Counter.objects.get(pk=1)}
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         return HttpResponse(json.dumps({'lat' : 5, 'lon': 5}))
        
# class Finder(generic.DetailView):
#     longitude = models.IntegerField()
#     latitude = models.IntegerField()
#     template_name = "home/index.html"

#     treeInfo = models.ListCharField(
#         base_field = models.CharField(max_length = 30),
#         size = 18,
#         max_length = (18 * 31)
#     )

#     def get(self, request, *args, **kwargs):
#         # context = {'lat' : }
#         return render(request, self.template_name, context)
    
#     def post(self, request, *args, **kwargs):
#         mydb = sqlite3.connect('../../tree_database.db')
#         mycursor = mydb.cursor()
#         treeInfo = nearest(mycursor,self.latitude,self.longitude)
#         treeInfo.save()

#         return redirect('homepage')

