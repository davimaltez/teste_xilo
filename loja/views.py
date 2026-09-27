from django.shortcuts import render
from .models import Produto


def home(request):

    produtos = Produto.objects.filter(
        ativo=True
    ).prefetch_related(
        'imagens',
        'variacoes'
    ).select_related(
        'categoria',
        'colecao'
    )

    return render(
        request,
        'loja/index.html',
        {'produtos': produtos}
    )