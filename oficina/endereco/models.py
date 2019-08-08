from django.db import models

# Create your models here.

class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'



class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    sigla = models.CharField(max_length=2)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, related_name='pais')

    def __str__(self):
        return self.pais.nome +' / ' +  self.nome

    class Meta:
        unique_together = ('pais','nome')


class Viagem(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    paises = models.ManyToManyField(Pais, related_name='pais_viagem')
    data = models.DateTimeField()


    def save(self, *args, **kwargs):
        print("KKKKKK")
        super(Viagem, self).save(*args, **kwargs)


    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Viagem'
        verbose_name_plural = 'Viagens'