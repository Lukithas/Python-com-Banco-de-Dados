# Gerenciador de Cargos e Empregados em Python

Este é um script de linha de comando (CLI) em Python que utiliza a biblioteca mysql-connector para gerenciar um banco de dados MySQL simples. O projeto permite cadastrar cargos e empregados, vinculando um empregado a um cargo específico.

Ele oferece operações básicas de CRUD (Criar, Ler, Atualizar, Excluir) e consultas com JOIN através de um menu interativo no terminal.

## 🚀 Funcionalidades

  * Conexão com MySQL: Estabelece uma conexão segura com um servidor de banco de dados MySQL.

  * Criação da Estrutura: Cria o banco de dados (db_cadastro) e as tabelas (tb_cargo, tb_empegrado) automaticamente se não existirem.

  *  Menu Interativo: Facilita a interação do usuário, que pode escolher a operação desejada através de comandos simples.

  *  Operações CRUD Completas:

       * [c] Create: Cria as tabelas no banco de dados.

       * [i] Insert: Adiciona novos cargos ou empregados.

       * [r] Select: Lista todos os registros de uma tabela.

       * [u] Update: Atualiza informações de cargos ou empregados.

       * [d] Delete: Remove registros do banco de dados.

   * Consulta com JOIN:

       * [j] Join: Exibe uma lista de empregados com os nomes de seus respectivos cargos, combinando dados das duas tabelas.

## 🛠️ Pré-requisitos

Antes de começar, garanta que você tenha os seguintes itens instalados:

  * Python 3.x

  * Um servidor MySQL (como MySQL Community Server, MariaDB, XAMPP, etc.) em execução.

  *  A biblioteca mysql-connector-python.

Para instalar a biblioteca, execute o seguinte comando no seu terminal:

pip install mysql-connector-python

⚙️ Como Usar

  1. Clone o Repositório


git clone https://github.com/seu-usuario/Python-com-Banco-de-Dados.git
cd Python-com-Banco-de-Dados

2. Configure a Conexão com o Banco de Dados
Abra o arquivo duas_tabelas.py e altere as credenciais na função create_connection() para que correspondam à sua configuração local do MySQL.
~~~Python
def create_connection():
    conexao = mysql.connector.connect(user='seu_usuario',
                                      password='sua_senha',
                                      host='localhost',)
    print('Conexão aberta!', conexao)
    return conexao
~~~
3. Execute o Script
Abra um terminal na pasta do projeto e execute o seguinte comando:


    python duas_tabelas.py

4. Siga as Instruções do Menu:

  * Na primeira execução, digite c para criar as tabelas.

  * Depois, utilize i para inserir cargos e empregados.

  * Utilize as outras opções (r, u, d, j) para gerenciar os dados.

  * Para finalizar, digite s para sair e fechar a conexão.

🗃️ Estrutura do Banco de Dados

O script gerencia duas tabelas com o seguinte esquema:

Tabela tb_cargo

Coluna	| Tipo	| Descrição
------  | ----- | --------
identificador| 	INT |	Chave Primária, Auto Incremento
nome|	VARCHAR(50) |	Nome do cargo (obrigatório)

Tabela tb_empegrado

Coluna |	Tipo	| Descrição
------- | -------- | ----------
identificador	| INT |	Chave Primária, Auto Incremento
nome| 	VARCHAR(50) |	Nome do empregado (obrigatório)
data_nascimento| 	DATE |	Data de nascimento do empregado
genero| 	ENUM('m', 'f')| 	Gênero do empregado (obrigatório)
cod_cargo| 	INT |	Chave Estrangeira que referencia tb_cargo(identificador)

