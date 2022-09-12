from django.db import models
from posts.models import Post
from django.contrib.auth.models import User


class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=50)
    email_comentario = models.EmailField()
    comentario = models.TextField()
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    data_comentario = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome_comentario
