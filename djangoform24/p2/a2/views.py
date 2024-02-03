from django.shortcuts import render
from django.http import HttpResponse



def menu(request):
    return HttpResponse('''
                        
                        
                        <h1>this is our menu page</h1>
                        
                       
                        <a href="/a2/wellcome/"> wellcome </a>
                        <a href="/a1/contact/"> contact </a>
                        <a href="/a1/feed/"> feed </a>
                        
                        
                        
                        
                        ''')


def wellcome(request):
    return HttpResponse('''
                        
                        
                        <h1>this is our wellcome page</h1>
                        
                        <a href="/a2/menu/">menu </a>
                       
                        <a href="/a1/contact/"> contact </a>
                        <a href="/a1/feed/"> feed </a>
                        
                        
                        
                        
                        ''')