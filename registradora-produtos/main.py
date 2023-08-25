#Ana Luísa S. Lopes 
#190102110

import sqlite3

data = sqlite3.connect('banco.db') #Conecta com o banco de dados
cur = data.cursor() 

cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='estoque' ''') #Verifica se existe a tebela estoque

if cur.fetchone()[0] != 1 : #Se não tem cria a tabela
    cur.execute("CREATE TABLE IF NOT EXISTS estoque(id INTEGER,produto TEXT NOT NULL,quantidade INTEGER,valor REAL) ")
    cur.execute("INSERT INTO estoque VALUES(1,'Camisa',3,40.00), (2,'Blusa',5,10.00)")

data.commit()

#Função lista estoque
def listEstoque():
    cur.execute("SELECT * FROM estoque")
    itens = cur.fetchall() #Seleciona todos os dados da tabela

    for item in itens: 
        print("ID: " + str(item[0]) + " - " + item[1]  + ": " +
        str(item[2]) + "  unidades " + " por R$ " + str(item[3]))
    data.commit()

#Função adiciona item na tabela
def adicionarItem(produto,quantidade,valor):
    cur.execute("SELECT * FROM estoque")
    items = cur.fetchall() #Seleciona todos os dados da tabela
    size = len(items) #Verifica qual o tamanho da tabela
    id = items[size - 1][0] + 1 #Pega o ID do último elemento e soma 1
 
    cur.execute("""INSERT INTO estoque VALUES(?,?,?,?);""", (id, produto, quantidade, valor))
    data.commit()

#Remove produto
def removerItem(id):
    cur.execute("SELECT * FROM estoque WHERE id = ?",id) # Seleciona o elemento com ID específico
    item = cur.fetchall() 

    if item[0][2] != 0: #Verifica a quantidade no estoque
        print(" A quantidade no estoque é " + str(item[0][2]) + ".\n" 
        + " Tem certeza que deseja REMOVER? S/N")
        opcao = input()

        if opcao == 'S':
            cur.execute('DELETE FROM estoque WHERE id=?', id) 
        else:
            print(" Produto não removido!")
            data.commit()
            return 0
    else:
        cur.execute('DELETE FROM estoque WHERE id=?', id)

    print(" Produto removido!")
    data.commit()

#Atualiza Produto
def atualizarItem(id, produto, quantidade, valor):
    cur.execute("SELECT * FROM estoque WHERE id = ?",id) #seleciona produto com id
    item = cur.fetchall()

    if produto == 'N' or produto == 'n': #Caso o nome do produto não seja alterado
        produto = item[0][1] #Permanece o nome anterior

    if quantidade == 'N' or quantidade == 'n': #Caso a quantidade do produto não seja alterado
        quantidade = item[0][2] #Permanece a quantidade anterior

    if valor == 'N' or valor == 'n': #Caso o preço não seja alterado
        valor = item[0][3] #Permanace o preço anterior
    
    #Atulaiza o banco de dados
    cur.execute('''UPDATE estoque SET produto=?, quantidade=?, valor=? WHERE id=?''', (produto,quantidade,valor,id))
    data.commit()

#Função realiza uma compra
def realizaCompra(id, quantidade):
    cur.execute("SELECT * FROM estoque WHERE id = ?",id) #Selelciona o elemento pelo ID
    item = cur.fetchall() 
    quantIten = item[0][2] 
    valor = item[0][3]
    
    #Compara a quantidade no estoque com a quantidade que quer comprar 
    if quantIten < quantidade:
        print('O produto tem apenas ' + str(quantIten) + ' unidades no estoque!')
        opcao = input("Deseja comprar as " + str(quantIten) + " unidades? S/N")

        if opcao == 'N' or opcao == 'n': #Caso não queira comprar a quantidade do estoque
            data.commit()
            return 0

        else: #Caso queira comprar a quantidade do estoque
            valor =  quantIten * valor #Preço da compra
            quantIten = 0 #Quantidade final do estoque
            cur.execute('''UPDATE estoque SET quantidade=? WHERE id=?''', (quantIten,id)) #Atualiza banco de dados
            data.commit()
            return valor

    valor =  quantidade * valor #Preço da compra
    quantIten = quantIten - quantidade #Quantidade final do estoque
    cur.execute('''UPDATE estoque SET quantidade=? WHERE id=?''', (quantIten,id)) #Atualiza banco de dados
    
    data.commit()
    return valor

#Verifica estoque baixo
def verificaEstoque():
    cur.execute("SELECT * FROM estoque") #Seleciona todos os elementos do estoque
    itens = cur.fetchall() 
    contador = 0 #Para não enviar a mesngem de Atenção varias vezes

    #Verifica todos os elementos
    for item in itens: 
        quantidade = item[2]
        if quantidade <= 3: #Se a quantidade for menor que 3
            if contador == 0: #Envia a mensagem uma vez
                print('--------------------------------------------------------')
                print('ATENÇÃO: os seguintes produtos estão com estoque baixo: ')
                contador = contador + 1
            #Infroma o produto, quantidade e ID
            print(item[1] + " (ID: " + str(item[0]) + ") - "  +
            str(item[2]) + "  unidades " )

    contador = 0
    data.commit()


def main():
    
    while(True): 
        print('\n  CONTROLE DE ESTOQUE \n')
        verificaEstoque()

        print('\n0 - Sair')
        print('1 - Listar estoque')
        print('2 - Adicionar Item')
        print('3 - Remover Item')
        print('4 - Atualizar Item')
        print('5 - Realizar Compra') 
        print('\n')

        opcao = input("Digite a opção: ")

        match opcao:
            case '0':
                cur.close()
                return 0
            case '1':
                listEstoque()
            case '2':
                produto = input('Nome do produto: ')
                quantidade = input('Quantidade: ')
                valor = input("Preço: ")
                adicionarItem(produto, quantidade, valor)
                print("  Produto Adicionado!")
            case '3':
                id = input('ID do produto: ')
                removerItem(id)
            case '4':
                id = input('ID do produto: ')
                print('Digite N para não ter alteração.')
                produto = input('Nome do produto: ')
                quantidade = input('Quantidade: ')
                valor = input("Preço: ")
                atualizarItem(id,produto,quantidade,valor)
            case '5': 
                id = input('Id do produto: ')
                quantidade = int(input('Quantidade: '))

                valor = str(realizaCompra(id,quantidade))
                print('Valor a pagar:  ' + valor)
    
main()
