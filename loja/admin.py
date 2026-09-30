from django.contrib import admin
from .models import (
    Categoria,
    Colecao,
    Produto,
    ImagemProduto,
    VariacaoProduto,
)


admin.site.site_header = 'VEREDAS — Administração'
admin.site.site_title = 'VEREDAS'
admin.site.index_title = 'Painel da Loja'


class CamposAdminMixin:
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        field = super().formfield_for_dbfield(db_field, request, **kwargs)
        if field is not None:
            labels = {
                'descricao': 'Descrição',
                'preco': 'Preço (R$)',
                'colecao': 'Coleção',
                'slug': 'Identificador do endereço',
                'estoque': 'Quantidade disponível',
            }
            field.label = labels.get(db_field.name, field.label)
            if db_field.name == 'slug':
                field.help_text = 'Preenchido a partir do nome. Deve ser único.'
        return field


@admin.register(Categoria)
class CategoriaAdmin(CamposAdminMixin, admin.ModelAdmin):

    list_display = (
        'nome',
        'slug',
    )

    prepopulated_fields = {
        'slug': ('nome',)
    }


@admin.register(Colecao)
class ColecaoAdmin(CamposAdminMixin, admin.ModelAdmin):

    list_display = (
        'nome',
        'slug',
        'ordem',
    )

    fields = ('nome', 'slug', 'descricao', 'imagem', 'ordem')
    ordering = ('ordem', 'id')

    prepopulated_fields = {
        'slug': ('nome',)
    }

class ImagemProdutoInline(CamposAdminMixin, admin.TabularInline):

    model = ImagemProduto
    ordering = ('ordem', 'id')
    verbose_name = 'imagem'
    verbose_name_plural = 'Imagens dos produtos'
    extra = 1
    fields = (
        'imagem',
        'ordem',
    )


class VariacaoProdutoInline(CamposAdminMixin, admin.TabularInline):

    model = VariacaoProduto
    verbose_name = 'tamanho'
    verbose_name_plural = 'Estoque e tamanhos'
    extra = 1
    fields = (
        'tamanho',
        'estoque',
    )

@admin.register(Produto)
class ProdutoAdmin(CamposAdminMixin, admin.ModelAdmin):

    list_display = (
        'nome',
        'preco',
        'categoria',
        'colecao',
        'ativo',
        'destaque',
        'ordem',
    )

    list_editable = ('preco', 'ativo', 'destaque', 'ordem')
    list_select_related = ('categoria', 'colecao')
    ordering = ('-destaque', 'ordem', 'id')

    fieldsets = (
        ('Informações principais', {
            'fields': ('nome', 'descricao', 'preco'),
        }),
        ('Organização da loja', {
            'fields': ('categoria', 'colecao', 'ativo', 'destaque', 'ordem'),
            'description': 'Ativo exibe o produto na loja. Destaque coloca o produto antes dos demais.',
        }),
        ('Endereço do produto', {
            'fields': ('slug',),
            'classes': ('collapse',),
        }),
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
class ImagemProdutoAdmin(CamposAdminMixin, admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        return super().changelist_view(
            request,
            extra_context={'title': 'Imagens dos produtos', **(extra_context or {})},
        )

    list_display = (
        'produto',
        'ordem',
    )

    list_filter = (
        'produto',
    )


@admin.register(VariacaoProduto)
class VariacaoProdutoAdmin(CamposAdminMixin, admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        return super().changelist_view(
            request,
            extra_context={'title': 'Estoque por tamanho', **(extra_context or {})},
        )

    search_fields = ('produto__nome',)
    list_select_related = ('produto',)

    list_display = (
        'produto',
        'tamanho',
        'estoque',
    )

    list_filter = (
        'tamanho',
    )