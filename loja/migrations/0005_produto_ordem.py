from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_remove_produto_estoque_remove_produto_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='ordem',
            field=models.PositiveIntegerField(
                default=0,
                help_text='Menores números aparecem primeiro, dentro de cada grupo de destaque.',
            ),
        ),
    ]
