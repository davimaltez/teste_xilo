from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_produto_ordem'),
    ]

    operations = [
        migrations.AddField(
            model_name='colecao',
            name='imagem',
            field=models.ImageField(
                verbose_name='Imagem da coleção',
                upload_to='colecoes/',
                blank=True,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name='colecao',
            name='descricao',
            field=models.TextField(verbose_name='Descrição', blank=True),
        ),
        migrations.AddField(
            model_name='colecao',
            name='ordem',
            field=models.PositiveIntegerField(
                default=0,
                help_text='Menores números aparecem primeiro.',
            ),
        ),
    ]
