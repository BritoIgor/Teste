from django.db import models

class Funcionario(models.Model):
    nome = models.CharField('nome', max_length=120)
    cpf = models.CharField('cpf', max_length=12)

    def __str__(self):
        return self.nome

class Configuracao(models.Model):
    horaEntrada = models.DateTimeField()
    horaSaida = models.DateTimeField()
    Funcionario = models.ForeignKey('Funcionario')

class Frequencia(models.Model):
    horaEntrada = models.DateTimeField()
    horaSaida = models.DateTimeField()
    CONSISTENTE = 'CO'
    INCONSISTENTE = 'IN'
    status = (
                (CONSISTENTE, 'Consistente'),
                (INCONSISTENTE, 'Inconsistente'),
            )
    status = models.CharField(max_length=2, choices = status, default=INCONSISTENTE)
    justificativa = models.TextField(blank=True, null=True)
    Funcionario = models.ForeignKey('Funcionario')
