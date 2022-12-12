from datetime import date
from random import randint
from Lab2.banco import *
from Lab2.interface.interface2 import checarEmail, cabecalho, leiaInt, menu


class Usuario:
    def __init__(self, cursor):
        self.cursor= cursor

    def get_usuario(self):
        self.cursor.execute('SELECT * FROM thayane_bitencourt.usuario')
        row = self.cursor.fetchall()
        return row


class Motorista:
    def __init__(self, cursor):
        self.cursor = cursor


    def get_motorista(self):
        self.cursor.execute('SELECT * FROM thayane_bitencourt.motorista')
        row = cursor.fetchall()
        return row


class Cartao:
    def __init__(self, cursor):
        self.cursor = cursor


    def get_cartao(self):
        self.cursor.execute('SELECT * FROM thayane_bitencourt.cartao')
        row = cursor.fetchall()
        return row


class Onibus:
    def __init__(self, cursor):
        self.cursor=cursor


    def get_onibus(self):
        self.cursor.execute('SELECT * FROM thayane_bitencourt.onibus')
        row = cursor.fetchall()
        return row






