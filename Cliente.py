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
 
# Função de Cifra de César para criptografar
def cifra_de_cesar(texto, deslocamento):
    criptografado = ""
    for char in texto:
        if 32 <= ord(char) <= 126:  # Considera apenas caracteres imprimíveis
            novo_char = chr((ord(char) - 32 + deslocamento) % 95 + 32)
        else:
            novo_char = char  # Mantém caracteres fora do intervalo imprimível inalterados
        criptografado += novo_char
    return criptografado
 
# Configuração do cliente
serverName = "10.1.70.17"
serverPort = 1700
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
 
# Cliente gera sua chave privada e pública
a = random.randint(1, p-1)  # Chave privada do cliente
A = (g ** a) % p  # Chave pública do cliente
 
# Envia a chave pública para o servidor
clientSocket.send(str(A).encode())
 
# Recebe a chave pública do servidor
B = int(clientSocket.recv(1024).decode())
 
# Calcula a chave secreta compartilhada
chave_simetrica = (B ** a) % p
print(f"🔑 Chave simétrica calculada pelo cliente: {chave_simetrica}")
 
# Enviar mensagem criptografada usando a chave simétrica como deslocamento
mensagem_original = "Olá, servidor! Esta é uma mensagem segura."
mensagem_criptografada = cifra_de_cesar(mensagem_original, chave_simetrica)
 
print(f"🔐 Mensagem original: {mensagem_original}")
print(f"🔏 Mensagem criptografada: {mensagem_criptografada}")
 
clientSocket.send(mensagem_criptografada.encode())
 
# Receber a resposta do servidor (mensagem em maiúsculas)
mensagem_maiusculas = clientSocket.recv(1024).decode()
print(f"📩 Mensagem recebida do servidor em maiúsculas: {mensagem_maiusculas}")
 
clientSocket.close()