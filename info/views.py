from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)

from .models import (
    Info,
    Licenses,
    Category,
    SubCategory,
    Forma,
    Comment,
)


class InfoDetailView(DetailView):
    model = Info


class CategoryDetailView(DetailView):
    model = Category


def index(request):
    cats = Category.objects.all()
    group = Group.objects.all
    context = {'cats': cats, 'cat_selected': 0, 'group': group}
    print(group)
    return render(request, 'info/index.html', context=context)


def show_category(request, cat_id):
    posts = Info.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'cat_selected': cat_id,
    }
    return render(request, 'info/posts.html', context=context)


class PostListView(ListView):
    model = Category
    template_name = 'info/index.html'
    context_object_name = 'all_posts'


class CategoryListView(ListView):
    model = Info
    template_name = 'info/blog.html'
    context_object_name = 'cat_post'


# -------------------Info

class InfoCreateView(LoginRequiredMixin, CreateView):
    model = Info
    fields = ['author', 'name',
              'image', 'num',
              'admin', 'country',
              'contact', 'cat',
              'licenses', 'forma',
              'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class InfoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Info
    fields = ['author', 'name',
              'image', 'num',
              'admin', 'country',
              'contact', 'cat',
              'licenses', 'forma',
              'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class InfoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Info
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class LicensesCreateView(LoginRequiredMixin, CreateView):
    model = Licenses
    fields = ['licenses']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class LicensesDetailView(DetailView):
    model = Licenses


class FormaCreateView(LoginRequiredMixin, CreateView):
    model = Forma
    fields = ['forma']

    def form_valid(self, form ):
        form.instance.author = self.request.user
        return super().form_valid(form)


class FormaDetailView(DetailView):
    model = Forma

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['img', 'name', 'content', 'slug']

    def form_valid(self, form ):
        form.instance.author = self.request.user
        return super().form_valid(form)







#
#
# class FormUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Forma
#     fields = ['forma']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
#
#
# class FormDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Forma
#     success_url = '/'
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
#
#
# #------------------------Forma
# class FormCreateView(LoginRequiredMixin, CreateView):
#     model = Forma
#     fields = ['forma']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#
# class FormUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Forma
#     fields = ['forma']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
#
#
# class FormDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Forma
#     success_url = '/'
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False



