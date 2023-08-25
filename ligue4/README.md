# Desafio 1–Ligue-4 em Python
Ligue-4 é um jogo simples que consiste em 2 jogadores posicionando   peças   coloridas   de   forma   alternada   em   um tabuleiro composto por linhas e colunas. Ganha o jogador que conseguir alinhar 4 fichas da cor dele na horizontal, na vertical ou na diagonal.

![Ligue-4](https://a-static.mlcdn.com.br/450x450/jogo-lig-4-estrela/magazineluiza/181219900/8ffa2168c115a67937de596ffd491c20.jpg)

## Ligue-4 para 2 jogadores
Crie um arquivo chamado ligue4.py que, quando executado, iniciará uma partida de Ligue-4 no terminal para 2 pessoas jogarem. Seu código será composto das funções a seguir:

### 1. main()
Essa  é  a  função  principal.  Ela  iniciará  a  variável *board*,  que  será  o  tabuleiro  do jogo. *board* será  um  vetor  bidimensional,  onde  uma  dimensão  representará  as colunas e a outra representará as linhas.  
Logo  após,  a  função  chamará **printBoard(board)** para  printar  o  tabuleiro  no console e criará uma variável booleana **endGame** para verificar se o jogo terminou ou não.
Depois disso, se iniciará um loop que vai fazer com que os 2 jogadores joguem de forma alternada até ter um vencedor. Utilize as funções descritas a seguir para formar o turno dos jogadores corretamente.

### 2. printBoard(board)
Essa função receberá como parâmetro o tabuleiro eserá responsável por printaros elementosna tela corretamente. Printe os elementos de *board* como se fosse um tabuleiro de Ligue-4.

### 3. move(piece, board, player)
Essa função receberá como parâmetro a “peça” do jogador, o tabuleiro e o nome do jogador. No nosso caso, para simplificar, um jogador pode ter a peça ‘1’ ou ‘X’ e o outro a peça ‘2’ ou ‘Y’. O nome pode ser qualquer string que você quiser.  
Aqui é onde o turno do jogador deve ser computado. Pegue o input do player e verifique se ele é válido. O input é um número de 1 a 7 que indica em qual coluna a peça será colocada.Você só deve colocar a peça no lugar se o input for um número de 1 a 7 e se a coluna desejadanão estiver cheia.  
Se tudo estiver certo com o input, procure a posição correta onde “cairá” a peça e atualize o tabuleiro. A função retorna o tabuleiro atualizado.

### 4. checkWin(piece, board)
Essa função recebe os mesmos parâmetros *piece* e *board* da função **move(piece, board, player)** e serve para verificar se existe alguma combinação de 4 "pieces" no "board" que ocasione o fim do jogo. Ela deve ser  chamada  após  cada  jogadapara verificar se o jogo terminou.
Você deverá checar se existe alguma combinação de 4 na horizontal, na vertical e  na  diagonal.  Para  realizar  isso,  verifique  as  posições  do  tabuleiro  e procure  por sequências  de  forma  individual:  primeiro  na  horizontal,  depois  na  vertical,  depois em uma das duas diagonais e, por último, na outra diagonal

## Instalação
Siga estas etapas para instalar e executar o programa "NomeDoPrograma":

### 1. Clonar o Repositório: 
Abra um terminal e execute o seguinte comando para clonar o repositório do GitHub para o seu sistema:

`git clone https://github.com/Luisa-Lopes/python.git`

### 2.Acessar o Diretório: 
Navegue para o diretório recém-clonado:

`cd ligue4`

### 3. Instalar Dependências: 
Use o gerenciador de pacotes pip para instalar as dependências do programa:

`pip install`

### 4.Execução: 
Agora você pode executar o programa com o seguinte comando:

`python ligue4.py`