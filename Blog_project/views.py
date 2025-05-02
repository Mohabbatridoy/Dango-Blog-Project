from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect(reverse('app_blog:blog_list'))