from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def after(request):
  template = loader.get_template('after 30min.html')
  return HttpResponse(template.render())


def location(request):
  template = loader.get_template('location.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def menu(request):
  template = loader.get_template('menu.html')
  return HttpResponse(template.render())

def order(request):
  template = loader.get_template('order.html')
  return HttpResponse(template.render())

def ordersuc(request):
  template = loader.get_template('ordersuc.html')
  return HttpResponse(template.render())

def p(request):
  template = loader.get_template('p work.html')
  return HttpResponse(template.render())

def review(request):
  template = loader.get_template('review.html')
  return HttpResponse(template.render())