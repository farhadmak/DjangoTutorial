# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from .models import Counter
from django.db import models

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
    neighbourhood = models.CharField(max_length=100)

    def nearest(self, request, *args, **kwargs):
        return -1

'''
import mysql.connector

location = pos
long = pos.x
lati = pos.y

mydb = mysql.connector.connect(
    host = "",
    user = "",
    passwd = "",
    database = ""
)

mycursor = mydb.cursor()

mycursor.execute("
SELECT *
FROM tree
ORDER BY sqrt( (lat - orig_lat)**2 + (long - orig_long)**2 ) DESC
LIMIT 1;
")
'''