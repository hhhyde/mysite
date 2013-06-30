# Create your views here.
from django.http import HttpResponse
from django.http import Http404
#from django.views.generic.simple import direct_to_template
from django.template.base import TemplateDoesNotExist

def about_pages(request, page):
    pass
#    try:
#        return direct_to_template(request, template = 'about/%s.html' % page)
#    except TemplateDoesNotExist:
#        raise Http404