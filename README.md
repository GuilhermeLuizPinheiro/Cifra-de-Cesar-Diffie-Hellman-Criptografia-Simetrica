PROJETO: Implementação de Servidor e Cliente TCP com Cifra de César e Diffie-Hellman

Descrição

Este repositório contém a implementação de um servidor e um cliente TCP em Python, com funcionalidades adicionais de criptografia usando a Cifra de César e troca de chaves seguras utilizando o algoritmo de Diffie-Hellman. 
O projeto foi desenvolvido como parte da atividade da disciplina ministrada pelo professor Fábio Henrique Cabrini na Faculdade de Tecnologia Engenheiro Salvador Arena, no curso de Engenharia da Computação (10º semestre).

Objetivos

1. Testar a comunicação entre cliente e servidor TCP em máquinas distintas utilizando Wireshark para monitoramento do fluxo de informações.
2. Implementar criptografia no fluxo de informações entre cliente e servidor utilizando a Cifra de César, sem uso de bibliotecas externas.
3. Implementar o algoritmo de Diffie-Hellman para troca segura de chaves simétricas.
4. Testar e validar os algoritmos de verificação de números primos, "Primo Fast" e "Primo Slow".

Estrutura do Repositório
/
|-- SimpleTCPServer.py # Servidor TCP com criptografia e troca de chaves
|-- SimpleTCPclient.py # Cliente TCP com criptografia e troca de chaves
|-- README.md # Documentação do projeto
|-- primo_fast.py # Algoritmo eficiente para verificação de números primos
|-- primo_slow.py # Algoritmo menos eficiente para verificação de números primos

Como Executar

1. Configuração do Ambiente
- Certifique-se de ter o Python instalado (versão 3.x recomendada).
- Clone este repositório:
 git clone https://github.com/GuilhermeLuizPinheiro/Cifra-de-Cesar-Diffie-Hellman-Criptografia-Simetrica
 cd seu-repositorio

2. Executar o Servidor
No terminal, execute o seguinte comando na máquina onde o servidor será executado:
 python SimpleTCPServer.py

3. Executar o Cliente
Em outra máquina ou no mesmo ambiente, execute o cliente com:
 python SimpleTCPclient.py

4. Testar os Algoritmos de Números Primos
Para testar a eficiência dos algoritmos de verificação de primos:
 python primo_fast.py
 python primo_slow.py

Exemplo de Saída
- Cifra de César: O cliente envia uma mensagem criptografada, e o servidor a decripta antes de exibir.
- Diffie-Hellman: Cliente e servidor estabelecem uma chave simétrica segura para comunicação criptografada.
- Testes de primos: Mostra o tempo de execução e confirma se um número é primo ou não.

Prazos e Entrega
A demonstração do funcionamento dos códigos será realizada em aula no dia 21/02. O repositório do GitHub contendo os arquivos deve ser entregue até 21/02 às 23h45 pelo formulário fornecido pelo professor.
Autor
- Guilherme Luiz Pinheiro Costa, Wesley Oliveira, Duarte Barbosa, Dayane Damaceno

Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para utilizar e modificar o código conforme necessário.
