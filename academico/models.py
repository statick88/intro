from django.db import models

class Curso(models.Model):
    
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveIntegerField()

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.nombre, self.creditos)