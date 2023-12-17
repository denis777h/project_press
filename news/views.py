from urllib import response, request

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.template.defaultfilters import censor
from .models import NewsArticle





class NewsListView(ListView):
    model = NewsArticle
    template_name = 'default.html'
    context_object_name = 'default'
    ordering = ['-publication_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['censor'] = censor
        return context


class NewsDetailView(DetailView):
    model = NewsArticle
    template_name = 'default.html'
    context_object_name = 'news_article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['censor'] = censor
        return context
