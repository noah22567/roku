from django.views.generic import TemplateView
from .my_roku import post_command as rc
# Create your views here.

from django.views.generic.base import View
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# class remote(TemplateView):
def remote(request):

    # template_name = "index.html"
    ip = "10.0.0.164"
    scheme = 'http://'
    keypress = ":8060/keypress/"
    launch = ":8060/launch/"

    url = scheme+ip

    context = {'url':url,'keypress':keypress,'launch':launch}

    # return render(context, "index.html")
    template = loader.get_template('index.html')

    return HttpResponse(template.render(context, request))





