from django.contrib import admin
from .models import (
    Categoria,
    Colecao,
    Produto,
    ImagemProduto,
    VariacaoProduto,
)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'slug',
    )

    prepopulated_fields = {
        'slug': ('nome',)
    }


@admin.register(Colecao)
class ColecaoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'slug',
    )

    prepopulated_fields = {
        'slug': ('nome',)
    }

class ImagemProdutoInline(admin.TabularInline):

    model = ImagemProduto
    extra = 1
    fields = (
        'imagem',
        'ordem',
    )


class VariacaoProdutoInline(admin.TabularInline):

    model = VariacaoProduto
    extra = 1
    fields = (
        'tamanho',
        'estoque',
    )

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'categoria',
        'colecao',
        'preco',
        'ativo',
        'destaque',
    )

    list_filter = (
        'categoria',
        'colecao',
        'ativo',
        'destaque',
    )

    search_fields = (
        'nome',
        'descricao',
    )

    prepopulated_fields = {
        'slug': ('nome',)
    }

    inlines = [
        ImagemProdutoInline,
        VariacaoProdutoInline,
    ]


@admin.register(ImagemProduto)
class ImagemProdutoAdmin(admin.ModelAdmin):

    list_display = (
        'produto',
        'ordem',
    )

    list_filter = (
        'produto',
    )


@admin.register(VariacaoProduto)
class VariacaoProdutoAdmin(admin.ModelAdmin):

    list_display = (
        'produto',
        'tamanho',
        'estoque',
    )

    list_filter = (
        'tamanho',
    )