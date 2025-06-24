from django.shortcuts import render, redirect, get_object_or_404
from .models import Mesa
from .forms import MesaForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def index(request):
    return render(request, 'mesas/index.html')

def lista_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesas/lista_mesas.html', {'mesas': mesas})

@login_required
def add(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            mesa = form.save(commit=False)
            mesa.mestre = request.user  # Assign the logged-in user to the mestre field
            mesa.save()
            return redirect('lista_mesas')
    else:
        form = MesaForm()
    return render(request, 'mesas/add.html', {'form': form})

@login_required
def edit(request, id):
    mesa = get_object_or_404(Mesa, pk=id)
    if mesa.mestre != request.user:
        return HttpResponseForbidden("Você não tem permissão para editar esta mesa.")
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect('lista_mesas')
    else:
        form = MesaForm(instance=mesa)
    return render(request, 'mesas/edit.html', {'form': form})

@login_required
def delete(request, id):
    mesa = get_object_or_404(Mesa, pk=id)
    if mesa.mestre != request.user:
        return HttpResponseForbidden("Você não tem permissão para excluir esta mesa.")
    if request.method == 'POST':
        mesa.delete()
        return redirect('lista_mesas')
    return render(request, 'mesas/delete.html', {'mesa': mesa})
