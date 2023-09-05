from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        # Obtener el valor del parámetro 'sort' de la URL
        sort_order = self.request.GET.get('sort', 'desc')

        # Cambiar el orden de acuerdo al valor del parámetro 'sort'
        if sort_order == 'asc':
            return Post.objects.filter(activo=True).order_by('fecha')
        elif sort_order == 'a':
            return Post.objects.filter(activo=True).order_by('titulo')
        elif sort_order == 'z':
            return Post.objects.filter(activo=True).order_by('-titulo')
        else:
            return Post.objects.filter(activo=True).order_by('-fecha')
        
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/postindividual.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()