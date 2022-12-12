import re


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))

            if type(n) == int:
                return n
            else:
                print("Não validado.")
                n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m ERRO. Digite por gentileza um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31m O usuário optou por sair sem digitar.\033[m')
            return 0
        else:
            return n


def leiaString(texto):
    while True:
        entrada = input(f'{texto}')
        if entrada.strip() != '':
            try:
                a = int(entrada)
                print('\033[31m ERRO. Não digitar números.\033[m')
            except:
                return entrada
        else:
            print('\033[31m ERRO.\033[m')


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('\033[35mBEM VINDO AO CADUni!\033[m')
    print('\033[35mSELECIONE A OPçÃO DESEJADA:\033[m')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())


def checarEmail():
    while True:
        try:
            regex = '^[a-z0-9\._a-z0-9]+[@]\w+[.]\w+[.]\w{2,3}$'

            email = str(input('E-mail:   '))

            if re.search(regex, email):
                print("Email válido")
                return email
            else:
                print("Email invalido")
                email = str(input('E-mail:   '))
        except (ValueError, TypeError):
            print('\033[31m ERRO. Digite por gentileza um email válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31m O usuário optou por sair sem digitar.\033[m')
            return 0




