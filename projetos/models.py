from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Projeto(models.Model):

    titulo = models.CharField(max_length=65,null=True,blank=True)
    descricao = models.TextField(null=True,blank=True)
    link = models.TextField(null=True,blank=True)
    category= models.ManyToManyField(Category)
    capa_img = models.ImageField(upload_to='capa/imagem/%Y/%m/%d/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    capa_video = models.FileField(upload_to='capa/video/%Y/%m/%d/',null=True,blank=True)   
    github = models.TextField(null=True,blank=True)
    exe = models.FileField( upload_to='exe/%Y/%m/%d/',null=True,blank=True)
    linux = models.FileField(upload_to='linux/%Y/%m/%d/',null=True,blank=True)
    apk = models.FileField( upload_to='apk/%Y/%m/%d/',null=True,blank=True)

