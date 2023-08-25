# Registradora de Produtos
O objetivo principal do desafio 2 será criar um sistema registrador de produtos conectadoa umbanco de dados através da linguagem de programação Python. Ele deverá ter 5funções básicas:

*1. Listar o estoque(listar_estoque);  
2. Adicionar um item(adicionar_item);  
3. Remove-lo(remover_item);   
4. Atualizá-lo(atualizar_item)  
5. Realizar compra (realizar_compra).*
  
Inicialmente,cria-seuma conexão ao banco de dadospara armazenar os produtos em estoque. Para este desafio,foi utilizada a biblioteca SQLite3[1],que possibilita criar um banco de dados de maneira simplificada e sem a necessidade de umservidor separado.  
Logo após a conexão, é verificado sea tabela de estoque já existee se está vazia. O programa deve ser capaz de criar uma tabela, caso não exista uma, epreenche-lacom produtos,caso esteja vazia.
O programa devera exibir uma tela de controle para que o usuário determine qual operação se deseja realizar no banco de dados e, de acordo com sua resposta, adeterminadafunção será executada.

### 1. listar_estoque()
Esta função terá dois trabalhos principais: uma busca de todos os registros na tabela do estoque e  uma exibição  de  cada  um  deles.Para  este  último,  é  necessário  elaborar  uma  estrutura  de repetição for que percorrerá a tabela e exibirá cada coluna em ordem de acordo com a linha de cada produto.
Ela deve exibir todos os itens em estoque, junto com seu id, a quantidade e o preço, ou seja,toda a tabela que foi montada, por isso não necessitará de parâmetros específicos.

### 2. adicionar_item(produto, quantidade, preco)
A função adicionar_itemdeve adicionar ao estoqueum produto qualquer. Esta função recebetrês parâmetros(produto, quantidade e preço),que especificaqual produto será adicionado, sua quantidadee seu preço. 

### 3.remover_item(id)
A funçãoremover_item recebe como parâmetro apenas o id do produto. Desta forma, a função devebuscar no estoque o id escolhido e remover todas informações referentes a ele(apagar a linha inteira dobanco de dados).
Para evitar problemas, será necessárioalertaro usuário sempre que um produto em estoque (Quantidade > 0)estiver sendo deletado.Deve ser solicitada uma confirmação para que a operação seja executada e o produto removido do estoque.

### 4. atualizar_item(id, produto=None, quantidade=None, preco=None)
A função atualizar_item serve para alterar as informações de um produto dentro do estoque. Esta funçãopode receber até4 parâmetros, sendo o idum parâmetro obrigatório ea base para identificarqual linha deve ser alterada. 
Para atualizar um item é necessário criar um método para que se verifique se determinada coluna deve alterada ou não, de acordo com os parâmetros inseridos ao se chamar a função.Sendo assim, se houver algum valor passado, o produto, a quantidade e/ou o preço devem ser alterados.

** IMPORTANTE:Qualquer  função  queacesse a  tabela  deestoque  (.db),  deve  primeiroiniciar  uma conexão com o banco de dados.Ao finalde qualquer operação, é necessário executar um commit()e encerrar a conexão com o estoque.**

## Desafio Bônus:

Criação deuma função verificar_estoque_baixo()que, definindo uma quantidade mínima paracada itemarmazenado, gera um alertaao usuáriosempre que algumproduto estiver nestelimite ou abaixo, indicandoo estoque em baixa.
Ela verificará a existência de algum produto com a quantidade menor que a determinada eobterá os seus dados,paraem seguidagerar o aviso

## INSTALAÇÃO
Siga estas etapas para instalar e executar o programa "NomeDoPrograma":

### 1. Clonar o Repositório: 
Abra um terminal e execute o seguinte comando para clonar o repositório do GitHub para o seu sistema:

`git clone https://github.com/Luisa-Lopes/python.git`

### 2.Acessar o Diretório: 
Navegue para o diretório recém-clonado:

`cd registradora-produtos`

### 3. Instalar Dependências: 
Use o gerenciador de pacotes pip para instalar as dependências do programa:

`pip install`

### 4.Execução: 
Agora você pode executar o programa com o seguinte comando:

`python main.py`