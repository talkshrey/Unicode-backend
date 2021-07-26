from django.http.response import HttpResponse, HttpResponseRedirect
from django import forms
from requests.api import request

# creating a class for a form
class SimpleForms(forms.Form):
  type = forms.IntegerField()
