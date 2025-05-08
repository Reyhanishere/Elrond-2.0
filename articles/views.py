from django.shortcuts import render
from django.urls import reverse_lazy
from articles.models import Article
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.

class ArticleListView(ListView):
    template_name = "articles/home.html"
    model = Article
    context_object_name = "articles"

    

class ArticleCreateView(CreateView):
    template_name = "articles/article_create.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.creator = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    template_name = "articles/article_update.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "article"


class ArticleDeleteView(DeleteView):
    template_name = "articles/article_delete.html"
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "article"