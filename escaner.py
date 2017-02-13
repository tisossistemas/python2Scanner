#!/usr/bin/python
#declarando utf-8
# -*- coding: utf-8 -*-
from os import system as comando
from sys import exit
from time import sleep
from socket import *

'''
@autor: Prince
@date: 13/02/2017
Scanner de portas criado para rodar em python e no sistema operacional windows
'''
def menu():
    comando('cls') #limpando a tela do pronpt
    print "--==== Port Scanner em Python ====--"
    try:
        escolha = int(input("Escolha: [1] Escanear  [2] Finalizar script :"))
    except:
        #se nao for escolhido nenhuma das duas opcoes o codigo apresenta um alerta aguarda alguns segundos limpa a tela e volta para o menu
        print "\nEscolha invalida"
        sleep(2)
        comando('cls')
        menu()
    if escolha == 1:
            #se a escolha for para escaner iniciamos o processo de escanner
        escanear()
    elif escolha == 2:
            #se a escolha for sair simplismente encerramos o pronpt
        comando("exit")
    else:
            #se a escolha for invalida apresentamos um alerta aguardamos alguns segundos e reinicimanos o menu
        print "\nEscolha invalida"
        sleep(1)
        menu()

def escanear():
        #limpando a tela e solicitando ao usuario o endereco para teste
    comando("cls") # limpando a tela
    host = raw_input(" Digite o host: ")
    executar = 'ping '+host

    try:
            #realizado um ping no endereco para verificar nossa conectividade, convertemos o endereco para um numero ip
        comando(str(executar))
        ip = gethostbyname(host)
        print "Endereco IP: %s" % (ip)
    except:
            #se o endereco for invalido apresentamos um alerta aguardamos alguns segundos limpamos a tela e voltamos para o escaner
        print "Host invalido."
        sleep(1)
        comando('cls')
        escanear()
    try:
            #pegando a porta inicial
        pi = int(input("Porta inicial (ex: 441): "))
    except:
            #se o numero for invaldio apresentamos um alerta aguardamos alguns segundos e reiniciamos o escaner
        print "Porta inicial invalida."
        sleep(1)
        comando('cls')
        escanear()
    try:
            #pegando a porta final
        pf = int(input("Porta final (ex: 449): "))
    except:
            #se a porta for invalida apresentamos um alerta aguardamos alguns segundos limpamos a tela e reiniciamos o escaner
        print "Porta final invalida."
        sleep(1)
        comando('cls')
        escanear()
    #iniciando o escnaeamento no loop entre as portas
    print "Iniciando escaneamento ....\n"



    for i in range(pi, pf + 1):
        sckt = socket(AF_INET, SOCK_STREAM)#criando um socket
        res = sckt.connect_ex((ip, i))#fazendo a conexao
        if (res == 0):
            print "Porta %d aberta" % (i)
        else:
            print "Porta %d fechada " %(i)
        sckt.close()
    print "\nEscaneamento finalizado\n"


menu()