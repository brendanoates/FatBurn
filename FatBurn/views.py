from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render
from FatBurn import settings
from FatBurn.helpers import ParagraphErrorList
from FatBurn.models import Person, Exercise
from django.http import HttpResponseRedirect
from .forms import UserDetailsForm
__author__ = 'boates'
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Home(View):
    def get(self, request):
        content = u'<h2>Page Content</h2><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis pharetra varius ' \
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
                  u'in felis sit amet augue.</p>'
        context = {'title':'Home', 'body_content':content}
        return render(request, 'fatburn/home.html',context)


class StartTheBurn(View):

    @method_decorator(login_required())
    def get(self, request):
        user = request.user
        exercises=Exercise.objects.all()

        context = {'title':'Start The Burn', 'exercises':exercises}
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

def userDetails(request):
    if request.method == 'GET':
        try:
            person, created = Person.objects.get_or_create(user=request.user)
            user = request.user
            if created:
                person.save()
            form = UserDetailsForm(
                initial={
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'start_weight': person.start_weight,
                    'height': person.height,
                },
            )
        except:
            pass

            #todo log this exception
        context = {'title':'Update Your Details', 'person':person, 'form':form }

        return render(request, 'fatburn/userDetails.html',context)

    else: #POST
        try:
            form = UserDetailsForm(data=request.POST, error_class=ParagraphErrorList)
            if form.is_valid():
                user = User.objects.get(id=request.user.id)
                person = Person.objects.get(user=user)
                user.first_name = form.cleaned_data.get('first_name', '')
                user.last_name = form.cleaned_data.get('last_name', '')
                person.start_weight = form.cleaned_data.get('start_weight', '')
                person.height = form.cleaned_data.get('height', '')
                user.save()
                person.save()
        except ValidationError:
            raise
        except:
            raise ValidationError("#Ooops an exception occurred during update. check logs for details")
            #todo log this exception
        context = {'title':'Updated Details', 'form':form}
    return render(request, 'fatburn/userDetails.html',context)
