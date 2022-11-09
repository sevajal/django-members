#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
    # first case: just "Hello world!"
    #return HttpResponse("Hello world!")

    # second case: Simple template:
    #template = loader.get_template('myfirst.html')
    #return HttpResponse(template.render())

    #third case: show data from table
    #mymembers = Members.objects.all().values()
    #output = ""
    #for x in mymembers:
    #    output += x["firstname"]
    #return HttpResponse(output)

    #fourth case: html table
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))

def testing(request):
  #mydata = Members.objects.all()
  #mydata = Members.objects.all().values()
  #mydata = Members.objects.values_list('firstname')
  #order by (ASC):
  #mydata = Members.objects.all().order_by('firstname').values()
  #order by (DESC):
  mydata = Members.objects.all().order_by('-lastname').values()
  #order by two(ASC):
  #mydata = Members.objects.all().order_by('lastname', 'firstname').values()
  #filter:
  #mydata = Members.objects.filter(firstname='Sebastian').values()
  #filter like S%:
  #mydata = Members.objects.filter(firstname__startswith='S').values()
  #filter AND:
  #mydata = Members.objects.filter(lastname='Carvajal', id=7).values()
  #filter OR:
  #mydata = Members.objects.filter(firstname='Sebastian').values() | Members.objects.filter(firstname='Pedro').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))