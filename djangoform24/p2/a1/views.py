from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
  return HttpResponse('''
                        
                        
                        <h1>this is our contact page</h1>
    
                        <a href="/a2/menu/">menu </a>
                        <a href="/a2/wellcome/"> wellcome </a>
                        
                        <a href="/a1/feed/"> feed </a>
                        
                        
                        
                        
                        ''')



def feedback(request):
   return HttpResponse('''
                        
                        
                        <h1>this is our feedback page</h1>
                        
                        <a href="/a2/menu/">menu </a>
                        <a href="/a2/wellcome/"> wellcome </a>
                        <a href="/a1/contact/"> contact </a>
                        
                        
                        
                        
                        
                        ''')
