from socket import *
import random
import time

# Função para verificar se um número é primo (Primo Fast)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Parâmetros públicos de Diffie-Hellman
p = 23  # Número primo
g = 5   # Base geradora

# Verificação se p é primo
start_time = time.time()
if not is_prime(p):
    print(f"{p} não é primo! Escolha outro número.")
    exit()
print(f"{p} é primo!")
end_time = time.time()
print(f"Tempo de execução: {end_time - start_time:.6f} segundos")

# Função para descriptografar a Cifra de César
def decifra_de_cesar(texto, deslocamento):
    descriptografado = ""
    for char in texto:
        if 32 <= ord(char) <= 126:  # Apenas caracteres imprimíveis
            novo_char = chr((ord(char) - 32 - deslocamento) % 95 + 32)
        else:
            novo_char = char  # Mantém caracteres inalterados
        descriptografado += novo_char
    return descriptografado

# Função para converter texto para maiúsculas
def para_maiusculas(texto):
    return texto.upper()

# Configuração do servidor
serverPort = 1700
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)

print("🔵 Servidor esperando conexões...\n")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"🔗 Conexão estabelecida com {addr}")

    # Servidor gera sua chave privada e pública
    b = random.randint(1, p-1)  # Chave privada do servidor
    print(f"🔗 Chave privada do servidor: { b }")
    B = (g ** b) % p  # Chave pública do servidor

    # Recebe a chave pública do cliente
    A = int(connectionSocket.recv(1024).decode())

    # Envia a chave pública do servidor para o cliente
    connectionSocket.send(str(B).encode())

    # Calcula a chave secreta compartilhada
    chave_simetrica = (A ** b) % p
    print(f"🔑 Chave simétrica calculada pelo servidor: {chave_simetrica}")

    # Receber a mensagem criptografada do cliente
    mensagem_recebida = connectionSocket.recv(1024).decode()
    print(f"📥 Mensagem recebida criptografada: {mensagem_recebida}")

    # Descriptografar a mensagem
    mensagem_descriptografada = decifra_de_cesar(mensagem_recebida, chave_simetrica)
    print(f"🔓 Mensagem descriptografada: {mensagem_descriptografada}")

    # Converter a mensagem para maiúsculas
    mensagem_maiusculas = para_maiusculas(mensagem_descriptografada)
    print(f"🔠 Mensagem convertida para maiúsculas: {mensagem_maiusculas}")

    # Enviar a mensagem em maiúsculas de volta para o cliente
    connectionSocket.send(mensagem_maiusculas.encode())

    # Fecha a conexão com o cliente, mas mantém o servidor rodando
    connectionSocket.close()
    print("🔄 Aguardando nova conexão...\n")
