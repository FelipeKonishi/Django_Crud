from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
def lista_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos\lista.html', {'produtos':produtos})

def cria_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm
    return render(request, 'produtos/form.html', {'form':form})

def edita_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/form.html', {'form': form})

def deleta_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/deleta.html', {'produto': produto})
    