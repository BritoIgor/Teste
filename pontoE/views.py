from django.shortcuts import render
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from pontoE.models import *
from django.contrib.auth.models import User
from pontoE.serializers import *

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class ConfiguracaoViewSet(viewsets.ModelViewSet):
    queryset = Configuracao.objects.all()
    serializer_class = ConfiguracaoSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer
