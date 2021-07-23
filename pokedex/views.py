from django.http.response import HttpResponse
#from django.shortcuts import render
import requests

# Create your views here.
def hello(request):
  return HttpResponse('Hello')

def pokFetcher(request):
  x = requests.get('https://pokeapi.co/api/v2/type/')
  result = x.json()
  database = result['results']
  names = []
  for i in database:
    name = i['name']
    names.append(name)

  return HttpResponse(names)
  