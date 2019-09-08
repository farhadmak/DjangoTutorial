# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
    model = Counter
    template_name = "home/index.html"

    def get(self, request, *args, **kwargs):
        context = {'our_counter' : Counter.objects.get(pk=1)}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        counter_object = Counter.objects.get(pk=1)
        counter_object.count += 1
        counter_object.save()
        return redirect('homepage')


class Finder(generic.DetailView):
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    
    def post(self, request, *args, **kwargs):
        mydb = sqlite3.connect('../../tree_database.db')
        mycursor = mydb.cursor()
        treeInfo = nearest(mycursor,self.latitude,self.longitude)

        return redirect('homepage')

    




