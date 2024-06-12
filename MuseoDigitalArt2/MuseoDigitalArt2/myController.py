from django.shortcuts import render
from django.http import HttpResponse
import json
from django.template import loader

def index(request):
  o1 = "<html> <body>"
  o2 = "<p>Welcome to DJANGO</p>"
  o3 = "</body> </html>"
  return HttpResponse(o1 + o2 + o3)

def index2(request):
  response = HttpResponse(content_type="text/html")
  response.write("<html> <body>")
  response.write("<p>Welcome to DJANGO again</p>")
  response.write("</body> </html>")
  return response

def params2json(request):
  if request.method == "GET":
    params = request.GET
  else:
    params = request.POST
  o = {}
  for n in params.dict().keys():
    o[n] = params.get(n)
  res = HttpResponse(content_type="application/json")
  res.write(json.dumps(o))
  return res

def noTemplate(request):
  f = open("/content/MuseoDigitalArt2/templates/template.html", "r")
  res = HttpResponse(content_type="text/html")
  res.write(f.read())
  return res

def template(request):
  template= loader.get_template("template.html")
  context= { "name": "John" }
  page = template.render(context, request)
  res = HttpResponse(content_type="text/html")
  res.write(page)
  return res

