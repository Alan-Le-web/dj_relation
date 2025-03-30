# Generated by Django 5.1.7 on 2025-03-30 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope_article_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
        migrations.AddField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag'),
        ),
    ]
