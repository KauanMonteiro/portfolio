from django.db import models

class Projeto(models.Model):

    titulo = models.CharField(max_length=65,null=True,blank=True)
    descricao = models.TextField(null=True,blank=True)
    link = models.TextField(null=True,blank=True)
    capa_img = models.ImageField(upload_to='capa/imagem/%Y/%m/%d/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    capa_video = models.FileField(upload_to='capa/video/%Y/%m/%d/',null=True,blank=True)   
    github = models.TextField(null=True,blank=True)
    executaveis = models.FileField( upload_to='executaveis/%Y/%m/%d/',null=True,blank=True)