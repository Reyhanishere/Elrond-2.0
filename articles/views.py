from django.shortcuts import render
from django.urls import reverse_lazy
from articles.models import Article
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