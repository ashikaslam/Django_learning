from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('''
                        
                        
                        <h1>this is our home page</h1>
                        
                        <a href="/a2/menu/">menu </a>
                        <a href="/a2/wellcome/"> wellcome </a>
                        <a href="/a1/contact/"> contact </a>
                        <a href="/a1/feed/"> feed </a>
                        
                        
                        
                        
                        ''')