from django.db import models
from django.contrib.auth.models import User


class Vaga(models.Model):
    #user = models.ForeignKey(
    #    User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Usuário")
    titulo = models.CharField(max_length=200, verbose_name="TÍTULO")
    atividades = models.TextField(null=True, blank=True, verbose_name="RESPONSABILIDADES E ATRIBUIÇÕES")
    requisitos = models.TextField(null=True, blank=True, verbose_name="REQUISITOS E QUALIFICAÇÕES")
    destaques = models.TextField(null=True, blank=True, verbose_name="VOCÊ SE DESTACA SE TIVER")
    ativo = models.BooleanField(default=True)
    #criado=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-ativo']

