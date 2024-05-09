from django.shortcuts import render, redirect

from .models import Nota

def home(request):
    notas = Nota.objects.all()
    return render(request, "index.html", {"notas" : notas})

def salvar(request):
    nome = request.POST.get("nome")
    Nota.objects.create(nome=nome)
    notas = Nota.objects.all()
    return render(request, "index.html", {"notas": notas})

def editar(request, id):
    notas = Nota.objects.get(id=id)
    return render(request, 'update.html', {"notas": notas})

def update (request, id):
    nome = request.POST.get("nome")
    notas = Nota.objects.get(id=id)
    notas.nome = nome
    notas.save()
    return redirect(home)

def deletar(request, id):
    notas = Nota.objects.get(id=id)
    notas.delete()
    return redirect(home)