import socket

IP = "127.0.0.1"
PORT = 12000

print('\n| ************************* Calculadora ************************* |\n| - Preencha os campos com "X" para SAIR. \n| - Insira os valores A e B, depois a OPERACAO que deseja realizar\n')

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    print(' Insira o valor A:')
    a = input()

    print(' Insira o valor B:')
    b = input()

    print(' Insira a OPERACAO aritmetica ("+", "-", "*", "/"):')
    operator = input()



    message = a +', '+b+', '+operator
    print(' Messagem sendo enviada para o servidor: ' + message + "\n")

    socket.sendto(message.encode('utf-8'), (IP, PORT))
    if a == 'X' or b == 'X' or operator == 'X':
        break

    data, address = socket.recvfrom(2048)
    text = data.decode('utf-8')
    print(' Resultado recebido do servidor %s \n Resposta: %s ' % (address, text) + "\n")

print('Conexao Finalizada!')
socket.close()
