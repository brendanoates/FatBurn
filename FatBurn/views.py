from django.shortcuts import render

__author__ = 'boates'
from django.http import HttpResponse
from django.views.generic import View
class Home(View):
    def get(self, request):
        content = u'<xmp><h2>Page Content</h2>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis pharetra varius ' \
                  u'quam sit amet vulputate.    Quisque mauris augue, molestie tincidunt condimentum vitae, gravida a ' \
                  u'libero. Aenean sit amet felis    dolor, in sagittis nisi. Sed ac orci quis tortor imperdiet venenatis. ' \
                  u'Duis elementum auctor accumsan.    Aliquam in felis sit amet augue.    <br>    Lorem ipsum dolor sit ' \
                  u'amet, consectetur adipiscing elit. Duis pharetra varius quam sit amet vulputate.    Quisque mauris ' \
                  u'augue, molestie tincidunt condimentum vitae, gravida a libero. Aenean sit amet felis    dolor, in ' \
                  u'sagittis nisi. Sed ac orci quis tortor imperdiet venenatis. Duis elementum auctor accumsan.    ' \
                  u'Aliquam in felis sit amet augue.    <br>    Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
                  u'Duis pharetra varius quam sit amet vulputate.    Quisque mauris augue, molestie tincidunt condimentum ' \
                  u'vitae, gravida a libero. Aenean sit amet felis    dolor, in sagittis nisi. Sed ac orci quis tortor ' \
                  u'imperdiet venenatis. Duis elementum auctor accumsan.    Aliquam in felis sit amet augue.    <br>    ' \
                  u'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis pharetra varius quam sit amet vulputate.    ' \
                  u'Quisque mauris augue, molestie tincidunt condimentum vitae, gravida a libero. Aenean sit amet felis    ' \
                  u'dolor, in sagittis nisi. Sed ac orci quis tortor imperdiet venenatis. Duis elementum auctor accumsan.    ' \
                  u'Aliquam in felis sit amet augue.    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ' \
                  u'pharetra varius quam sit amet vulputate.    Quisque mauris augue, molestie tincidunt condimentum vitae, ' \
                  u'gravida a libero. Aenean sit amet felis    dolor, in sagittis nisi. Sed ac orci quis tortor imperdiet ' \
                  u'venenatis. Duis elementum auctor accumsan.    Aliquam in felis sit amet augue.    <br>    Lorem ipsum ' \
                  u'dolor sit amet, consectetur adipiscing elit. Duis pharetra varius quam sit amet vulputate.    Quisque ' \
                  u'mauris augue, molestie tincidunt condimentum vitae, gravida a libero. Aenean sit amet felis    dolor, ' \
                  u'in sagittis nisi. Sed ac orci quis tortor imperdiet venenatis. Duis elementum auctor accumsan.    Aliquam ' \
                  u'in felis sit amet augue.    <br>    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ' \
                  u'pharetra varius quam sit amet vulputate.    Quisque mauris augue, molestie tincidunt condimentum vitae, ' \
                  u'gravida a libero. Aenean sit amet felis    dolor, in sagittis nisi. Sed ac orci quis tortor imperdiet ' \
                  u'venenatis. Duis elementum auctor accumsan.    Aliquam in felis sit amet augue.    <br>    Lorem ipsum ' \
                  u'dolor sit amet, consectetur adipiscing elit. Duis pharetra varius quam sit amet vulputate.    Quisque ' \
                  u'mauris augue, molestie tincidunt condimentum vitae, gravida a libero. Aenean sit amet felis    dolor, in ' \
                  u'sagittis nisi. Sed ac orci quis tortor imperdiet venenatis. Duis elementum auctor accumsan.    Aliquam ' \
                  u'in felis sit amet augue.</xmp>'
        context = {'title':'Home', 'body_content':content}
        return render(request, 'fatburn/home.html',context)

class StartTheBurn(View):
    def get(self, request):
        context = {'title':'Start The Burn'}

        return render(request, 'fatburn/startTheBurn.html',context)

class LoginRequired(View):
    def get(self, request):
        content = '''<p>To be able to access this page you are required to login, we use <a href="https://www.mozilla.org/persona/" target="_blank">Mozilla Persona</a> to manage this.</p>''' \
                  '''<p>Persona allows you to sign in to sites using any of your existing email addresses; and if you use Yahoo! or Gmail for email, you will be able to sign in without having to create a new password.</p>'''
        context = {'title':'Login Required', 'body_content':content}
        return render(request, 'fatburn/loginRequired.html',context)

class About(View):
    def get(self, request):
        context = {'title':'About'}
        return render(request, 'fatburn/about.html',context)