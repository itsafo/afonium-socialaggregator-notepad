# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template, forms
from .models import Post, Category
from .forms import PostForm

# Import function to create new note
from django.views.generic import CreateView, ListView, UpdateView, DetailView


# **** I HAVE DEPRECATED THIS CLASS AND USED "Notes" CLASS INSTEAD *****
# You can use this type of login authentication for a function
# But can't use this for a class
@login_required(login_url="/login/") # This is a decoratorto authenticate user
def index(request):
    # One good old style of programming functions
    # Define your context variable, then render
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "index.html", context)
# **************************************************************************


@login_required(login_url="/login/")
def panel(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "panels.html", context)


choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


# THis is the right Login authentication for a class
# Dont use a desorator
# Puting Creatview argument before ListView works for
# Having form and list of notes on the same page
class Notes(LoginRequiredMixin, CreateView, ListView):
    model = Post                        # Calling the model in the database
    template_name = 'app/notes.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'       # Assining a representation for the model in the html file
    ordering = ['-date_posted']
    fields = ['title', 'category', 'content']   # Required for the form

    # Colecting category data and creating nav links
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Notes, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu 
        return context 


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NoteDetail(CreateView, ListView):
    model =  Post
    template_name = 'app/post_detail.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    fields = ['title', 'category', 'content']
    
    widgets = {
        'category': forms.Select(choices=choices)
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewNote(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'category', 'content']
    # template_name = 'app/new_note.html'
    # context_object_name = 'posts'  


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateNote(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'category', 'content']

    widgets = {
        'category': forms.Select(choices=choices)
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class AddCategory(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'app/create.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

def CategoryView(request, pk_test):
    parent = Category.objects.get(id=pk_test)
    category_list = parent.post_set.all()
    form = PostForm()
    context = {
        'cat_name':parent,
        'cate':category_list,
        'form':form
    }
    return render(request, 'app/categorized_detail.html', context)
    #  ---- Working on updating notes -----------
    # fields = ['title', 'category', 'content']    
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
    # ----------------------------------
    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(CategoryView, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu 
    #     return context 


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))




# ---Deprecated libraries---
# from django.urls import reverse_lazy
# from .forms import BookModelForm
# For my ppopups:
# from bootstrap_modal_forms.generic import BSModalCreateView 

# --- Deprecated Codes ----
# Defining Choices for category
# choices = [('sports', 'sports'), ('motivation', 'motivation')]
# You might need to restart the server when you add new category from admin
# class BookCreateView(BSModalCreateView):
#     template_name = 'app/add_category_popup.html'
#     form_class = BookModelForm
#     success_message = 'Success: Book was created.'
#     success_url = reverse_lazy('notes')
