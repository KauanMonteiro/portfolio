# Generated by Django 5.0.7 on 2024-12-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='capa_img',
            field=models.ImageField(blank=True, null=True, upload_to='capa/imagem/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='capa_video',
            field=models.FileField(blank=True, null=True, upload_to='capa/video/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='github',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='tipo',
            field=models.CharField(blank=True, choices=[('video', 'Vídeo'), ('imagem', 'Imagem')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='titulo',
            field=models.CharField(blank=True, max_length=65, null=True),
        ),
    ]