from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import requests
from .forms import SimpleForms

# fetching all types of pokemons
def pokFetcher(request):
  x = requests.get('https://pokeapi.co/api/v2/type/')
  result = x.json()
  database = result['results']
  names = []
  for i in database:
    name = i['name']
    names.append(name)

  return HttpResponse(names)

# creating a simple form
def form(request):
  f = SimpleForms()
  store = render(request, 'index.html', {'form':f})
  return HttpResponse(store) 

# fetching all types of pokemons
def typeFetcher(request):
  url = 'https://pokeapi.co/api/v2/type/'
  t = requests.get(url)
  ans = t.json()
  data = ans['results']
  return render(request, 'form.html', {'list':data})