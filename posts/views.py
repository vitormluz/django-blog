from django.shortcuts import render
from django.views.generic import ListView, UpdateView


class PostIndex(ListView):
    template_name = 'posts/index.html'


class PostBusca(PostIndex):
    pass


class PostCategoria(PostIndex):
    pass


class PostDetalhes(UpdateView):
    pass
