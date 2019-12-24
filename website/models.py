from django.db import models

# Create your models here.
class cursos(models.Model):
    opcoes_de_cursos = [
        ('Inglês'),
        ('Francês'),
        ('Informática'),
    ] 

    nome = models.CharField(max_length=25)
    preco = models.DecimalField(decimal_places=2, max_digits=1000, default=149,99)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class cadastro_do_cliente(models.Model):
    
