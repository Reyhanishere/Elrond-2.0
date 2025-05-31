from django.shortcuts import render
from django.urls import reverse_lazy
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from articles.models import Article

from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _ # lan setting

from allauth.account.views import SignupView as AllauthSignupView

# Create your views here.

class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "articles/home.html"
    model = Article
    context_object_name = "articles"

    def get_queryset(self) -> QuerySet[Any]:
        return Article.objects.filter(creator=self.request.user).order_by("-created_at")

    

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "articles/article_create.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.creator = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "articles/article_update.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "article"

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator


class ArticleDeleteView(DeleteView):
    template_name = "articles/article_delete.html"
    model = Article
    success_url = reverse_lazy("home")
    
    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator
    
# lan setting
def my_view(request):
    message = _("This is a translated message.")

# class SignupView(CreateView):
#     template_name = "account/signup.html"
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")

class CustomSignupView(AllauthSignupView):
    template_name = "account/signup.html"
    success_url = reverse_lazy("login")