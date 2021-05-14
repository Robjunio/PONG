# Refatoração e debug do PONG!
No seguinte repositório, será feito a refatoração e debug do projeto PONG, de autoria do mestre Jucimar Silva Jr, 
além disso haverá a inserção de novas funcionalidades para a melhoria da jogabilidade em geral.

A seguir será disponibilizado o link do repositório original, https://github.com/jucimarjr/lpc_2021-2.git.

# Mudanças feitas:
Comparado ao original, o seguinte codigo tem alguns diferenciais:
- Correção do bug da raquete;
- Melhoria da raquete;
- Desenvolvimento de uma velocidade de jogo;
- Inserção da condição de vitoria; 
- Otimização e formatação do código a PEP-8.

# Observações:
O jogo foi desenvolvido para atender os três principais sistemas operacionais (Linux, Mac, Windows). Se seu S.O for Linux ou Mac você precisará realizar pequenas alterações no código referentes ao áudio do jogo.

Para Linux:
Passo 1
Abra o arquivo mypong.py em um editor, vá para a linha 2 do arquivo, você encontrará o seguinte comando:

# import os

Você deve remover o caractere '#' e o espaço antes da palavra import. A linha agora deve estar como abaixo:

import os

Agora vá para a linha 3 onde está o seguinte codigo:

from winsound import PlaySound, SND_ASYNC

Você deve adicionar ao começo dessa linha o caractere '#' e um único espaço, a nova linha deve estar como abaixo:

# from winsound import PlaySound, SND_ASYNC

Passo 2
Após isso vá para a linha 11, onde você encontrará o seguinte trecho:

# os.system("aplay bounce.wav&")  # On Linux

Você precisa novamente remover o caractere '#' e o espaço. No fim você deve ter o seguinte resultado:

os.system("aplay bounce.wav&")  # On Linux

Passo 3
Agora na linha 12 você encontrará:

PlaySound("bounce.wav", SND_ASYNC)  # On Windows

Agora você deve adicionar o caractere '#' e um espaço no inicio da linha, o codigo deve ficar como o exemplo abaixo:

# PlaySound("bounce.wav", SND_ASYNC)  # On Windows

Passo 4
Nas linha 16 e 20 você encontrará algo muito parecido com conteudo da linha do passo 2, e você repetirá os mesmos passos do passo 2 em ambas as linhas de código.

Passo 5
Nas linha 17 e 21 você encontrará algo muito parecido com conteudo da linha do passo 3, e você repetirá os mesmos passos do passo 3 em ambas as linhas de código.

Passo 6
Salve as alterações e você já pode rodar o jogo.

Para o Mac os passos são os seguintes:

Passo 1
Os passo aqui são identicos ao passo 1 da configuração para Linux.

Passo 2
Após isso vá para a linha 10, onde você encontrará o seguinte trecho:

# os.system("afplay bounce.wav&")  # On MAC

Você precisa novamente remover o caractere '#' e o espaço. No fim você deve ter o seguinte resultado:

os.system("afplay bounce.wav&")  # On MAC

Passo 3
Agora na linha 12 você encontrará:

PlaySound("bounce.wav", SND_ASYNC)  # On Windows

Agora você deve adicionar o caractere '#' e um espaço no inicio da linha, o codigo deve ficar como o exemplo abaixo:

# PlaySound("bounce.wav", SND_ASYNC)  # On Windows

Passo 4
Nas linha 15 e 19 você encontrará algo muito parecido com conteudo da linha do passo 2, e você repetirá os mesmos passos do passo 2 em ambas as linhas de código.

Passo 5
Nas linha 17 e 21 você encontrará algo muito parecido com conteudo da linha do passo 3, e você repetirá os mesmos passos do passo 3 em ambas as linhas de código.

Passo 6
Salve as alterações e você já pode rodar o jogo.
