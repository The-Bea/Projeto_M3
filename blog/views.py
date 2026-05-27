import asyncio
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def home_view(request):
    posts = Post.objects.filter(publicado=True).order_by('-data_criacao')
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})


async def async_view(request):
    print("=== [Início] Requisição assíncrona recebida no terminal ===")
    

    await asyncio.sleep(3)
    
    print("=== [Fim] Tarefa assíncrona finalizada com sucesso! ===")
    return HttpResponse("<h1>Exercício de Concorrência Django: View Assíncrona Funcionando!</h1>")