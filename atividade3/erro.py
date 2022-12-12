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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))

            if type(n) == float:
                return n
            else:
                print("Não validado.")
                n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31m ERRO. Digite por gentileza um número válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31m O usuário optou por sair sem digitar.\033[m')
            return 0
        else:
            return n