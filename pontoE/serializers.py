from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from pontoE.models import *
from django.conf.urls import url, include

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('nome', 'cpf')

    def create(self, validated_data):
        return Funcionario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance


class ConfiguracaoSerializer(serializers.HyperlinkedModelSerializer):
    funcionario = FuncionarioSerializer(many=False)
    class Meta:
        model = Configuracao
        fields = ('horaEntrada', 'horaSaida', 'funcionario')

    def create(self, validated_data):
        return Configuracao.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.horaEntrada = validated_data.get('horaEntrada', instance.horaEntrada)
        instance.horaSaida = validated_data.get('horaSaida', instance.horaSaida)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

class FrequenciaSerializer(serializers.HyperlinkedModelSerializer):
    funcionario = FuncionarioSerializer(many=False)
    class Meta:
        model = Frequencia
        fields = ('horaEntrada', 'horaSaida', 'status', 'justificativa', 'funcionario')

    def create(self, validated_data):
        return Frequencia.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.horaEntrada = validated_data.get('horaEntrada', instance.horaEntrada)
        instance.horaSaida = validated_data.get('horaSaida', instance.horaSaida)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
