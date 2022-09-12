from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_post = models.DateTimeField(auto_now_add=True)
    conteudo = models.TextField()
    trecho = models.CharField(max_length=350)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    imagem = models.ImageField(upload_to='imagens_posts/%Y/%m/%d')
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
