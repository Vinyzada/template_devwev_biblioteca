# Generated by Django 5.2.1 on 2025-07-01 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='status',
            field=models.IntegerField(choices=[(1, 'Carrinho'), (2, 'Finalizado'), (3, 'Pago'), (4, 'Entregue')], default=1),
        ),
        migrations.CreateModel(
            name='ItensCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='core.compra')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.livro')),
            ],
        ),
    ]
