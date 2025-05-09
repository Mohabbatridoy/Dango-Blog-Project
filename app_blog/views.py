from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, TemplateView, View, DeleteView
from django.urls import reverse, reverse_lazy
from app_blog.models import Blog, comment, Likes
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

# Create your views here.

class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'app_blog/create_blog.html'
    fields = ('blog_title','blog_content','blog_image')

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ","-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

class BlogList(LoginRequiredMixin, ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'app_blog/blog_list.html'