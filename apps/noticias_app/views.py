from unicodedata import category
from urllib import request
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from .models import Noticia, Comentario,Categoria
from django.contrib.auth.models import User
from django.http.response import Http404
from .forms import FormComment
from django.contrib.auth.decorators import login_required

def proyectos(request):
    return render(request, 'proyectos.html')

def donar(request):
    return render(request, 'donar.html')

def index(request):
    
    lista_noticias = Noticia.objects.all().order_by('-id')[:3]
    lista_user = User.objects.all()
    context = {
        "noticias": lista_noticias,
        "Usuarios": lista_user
    }
    return render(request, 'index.html', context)


def nosotros(request):
    return render(request, 'nosotros.html')



def notices(request):
    lista_categorias = Categoria.objects.all()
    lista_noticias = Noticia.objects.all().order_by('-id')
    context = {
        "categorias":lista_categorias,
        "noticias": lista_noticias
    }
    return render(request, 'notices.html', context)


def noticeDetail(request, id):
    try:
        noticia = Noticia.objects.get(id=id)
        lista_comentarios = Comentario.objects.filter(aprobado=True)
    except Noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')\
    
    form = FormComment()
    
    if (request.method == "POST") and (request.user.id != None):
        form = FormComment(request.POST)
        if form.is_valid():
            comment = Comentario(
                autor_id = request.user.id,
                cuerpo_comentario=form.cleaned_data["cuerpo_comentario"],
                noticia=noticia
            )
            comment.save()
            return redirect("Noticia", id=noticia.id)

    context = {
        "form":form,
        "noticia": noticia,
        "comentarios": lista_comentarios
    }
    return render(request, 'noticeDetail.html', context)

def categoriaDetail(request, id):

    try:
        lista_categorias = Categoria.objects.all()
        categoria = Categoria.objects.get(id = id)
        noticias = Noticia.objects.filter(categorias = id)
        lista_comentarios = Comentario.objects.filter(aprobado=True)
    except Noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')\
    
    form = FormComment()
    
    if (request.method == "POST") and (request.user.id != None):
        form = FormComment(request.POST)
        if form.is_valid():
            comment = Comentario(
                autor_id = request.user.id,
                cuerpo_comentario=form.cleaned_data["cuerpo_comentario"],
                noticia=noticias
            )
            comment.save()
            return redirect("Noticia")

    context = {
        "categori":categoria,
        "categorias":lista_categorias,
        "form":form,
        "noticias": noticias,
        "comentarios": lista_comentarios
    }
    return render(request, 'notices.html', context)


@login_required
def commentAproved(request, id):
    try:
        comentario = Comentario.objects.get(id=id)
    except Comentario.DoesNotExist:
        raise Http404("Inexistente")

    comentario.approve()
    return redirect("Noticia", id=comentario.noticia.id)
