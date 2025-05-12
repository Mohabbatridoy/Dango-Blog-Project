from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, TemplateView, View, DeleteView
from django.urls import reverse, reverse_lazy
from app_blog.models import Blog, Likes,Comment
from app_blog.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404
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
        cleaned_title = ''.join(e for e in title if e.isalnum() or e == ' ')
        cleaned_title = cleaned_title.replace(' ', '-').lower()
        blog_obj.slug = cleaned_title + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

class BlogList(LoginRequiredMixin, ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'app_blog/blog_list.html'


@login_required 
def blog_details(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
        comment_form = CommentForm()
        already_liked = Likes.objects.filter(blog=blog, user=request.user)
        if already_liked:
            Liked = True
        else:
            Liked = False
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.blog = blog
                comment.save()
                return HttpResponseRedirect(reverse('app_blog:blog_details', kwargs={'slug':slug}))
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    return render(request, 'app_blog/blog_details.html', context={'blog':blog, 'comment_form':comment_form, 'Liked':Liked})


@login_required
def Liked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    if not already_liked:
        liked_post = Likes(blog=blog, user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('app_blog:blog_details', kwargs={'slug':blog.slug}))

@login_required
def Unliked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('app_blog:blog_details', kwargs={'slug':blog.slug}))