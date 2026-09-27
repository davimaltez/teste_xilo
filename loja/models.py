from django.db import models


class Categoria(models.Model):

    nome = models.CharField(max_length=100)

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome


class Colecao(models.Model):

    nome = models.CharField(max_length=100)

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):

    nome = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    descricao = models.TextField(blank=True)

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='produtos'
    )

    colecao = models.ForeignKey(
        Colecao,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='produtos'
    )

    ativo = models.BooleanField(default=True)

    destaque = models.BooleanField(default=False)

    criado_em = models.DateTimeField(auto_now_add=True)

    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class ImagemProduto(models.Model):

    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name='imagens'
    )

    imagem = models.ImageField(
        upload_to='produtos/'
    )

    ordem = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Imagem de {self.produto.nome}"


class VariacaoProduto(models.Model):

    TAMANHOS = [
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G'),
        ('GG', 'GG'),
    ]

    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name='variacoes'
    )

    tamanho = models.CharField(
        max_length=2,
        choices=TAMANHOS
    )

    estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.produto.nome} - {self.tamanho}"