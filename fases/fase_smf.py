# -*- coding: utf-8 -*-
from os import path
import sys
import math

project_dir = path.dirname(__file__)
project_dir = path.join('..')
sys.path.append(project_dir)

from atores import PassaroAmarelo, PassaroVermelho, Obstaculo, Porco
from fase import Fase
from placa_grafica_tkinter import rodar_fase
from random import randint

if __name__ == '__main__':
    fase = Fase(intervalo_de_colisao=32)


    # Adicionar Pássaros Amarelos
    for i in range(4):
        fase.adicionar_passaro(PassaroAmarelo(30, 30))
        fase.adicionar_passaro(PassaroVermelho(30, 30))


    # Obstaculos
    _obstaculos = [(300,0),(400,40),(500,80),(600,120),(700,160)]
    for posicao_obstaculo in _obstaculos:
        x, y  = posicao_obstaculo
        fase.adicionar_obstaculo(Obstaculo(x, y))

    # Porcos
    _porcos = [(340,0),(440,0),(540,0),(640,0),(740,0)]
    for posicao_porco in _porcos:
        x, y = posicao_porco
        fase.adicionar_porco(Porco(x, y))

    rodar_fase(fase)