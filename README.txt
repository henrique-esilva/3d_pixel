Projeto 3d pixel

Esse script distorce imagens de acordo com a distância. Tinha assistido um vídeo sobre Mario Kart 64. Parece que os personagens do jogo não eram modelos 3d, mas imagens 2d com o tamanho distorcido. Fiquei curioso e quis produzir o mesmo efeito.

Há um artigo na Wikipedia sobre diâmetro angular. Uma grandeza que indica a parcela que um objeto ocupa na superfície arredondada da lente de uma câmera, ou do olho humano. É dado por um cálculo trigonométrico.

delta = arco tangente(d/R)

onde:
	delta é o ângulo ocupado pelo objeto, ou seja, o diâmetro angular (em pi radianos)
	d é o diâmetro transversal do objeto
	R é a distância entre o objeto e o observador

Para converter o diâmetro angular para graus, basta multiplicar o valor por 360 dividido por duas vezes o valor de pi, como abaixo:

delta (em graus) = delta (em pi radianos) * 360 / 2 * pi

simplificando:

delta (em gaus) = delta (em pi radianos) * 180 / pi



Implementei esta fórmula, criei uma tela em Pygame e apliquei a fórmula em um quadrado. Fiquei satisfeito com o código. Podia movimentar, por assim dizer, o quadrado em tempo de execução. Uma variável de distância aumentava e diminuía, e era usada no cálculo da fórmula para redimensionar o quadrado.

A função distorce o tamanho horizontal e o vertical da imagem individualmente.
tamanho horizontal * atan(d/R)*180/pi
tamanho vertical   * atan(d/R)*180/pi

Sendo assim, comecei a usar retângulos brancos. A intenção era criar um salão cheio de colunas. Então fiz um vetor de vetores no formato 100 x 100 (100 colunas e 100 fileiras). Cada valor 1 no vetor seria a posição de uma coluna. Um código na renderização afastava as colunas, para que pudessem ser distinguidas.

Depois de alguns testes, perccebi que a distorção estava errada. Como o arco tangente tem o crescimento atenuado conforme a tangente aumenta, a função estava programada para atenuar o crescimento da imagem conforme se aproximava. Em vez disso, ela deveria ser renderizada com no máximo o tamanho da própria tela, caso o diâmetro angular fosse igual à abrtura da câmera. O novo redimensionamento ficou assim:

(tamanho horizontal da tela / abertura horizontal da camera) * tamanho horizontal * atan(d/R)*180/pi
(  tamanho vertical da tela /   abertura vertical da câmera) *   tamanho vertical * atan(d/R)*180/pi
