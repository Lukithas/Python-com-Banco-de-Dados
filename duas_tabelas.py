import mysql.connector


def create_connection():
    conexao = mysql.connector.connect(user='root',
                                      password='Lep07161',
                                      host='localhost',
                                      auth_plugin='mysql_native_password')
    print('Conexão aberta!', conexao)
    return conexao

def create_database():
    sql = '''CREATE DATABASE IF NOT EXISTS db_cadastro'''
    sql_use = 'use db_cadastro'
    cursor.execute(sql)
    cursor.execute(sql_use)

def create_table():
    sql_cargo = '''CREATE TABLE IF NOT EXISTS tb_cargo(
            identificador INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50) NOT NULL
            )'''
    cursor.execute(sql_cargo)
    print('Tabela cargo criada com sucesso!')

    sql_empregado = '''CREATE TABLE IF NOT EXISTS tb_empregado(
             identificador INT AUTO_INCREMENT,
             nome VARCHAR(50) NOT NULL,
             data_nascimento DATE NULL,
             genero enum('m', 'f') NOT NULL,
             cod_cargo INT NOT NULL,
             PRIMARY KEY (identificador),
             FOREIGN KEY (cod_cargo) REFERENCES tb_cargo(identificador)
             )'''
    cursor.execute(sql_empregado)
    print('Tabela empregado criada com sucesso!')

def insert_cargo():
    v_nome_cargo = input('Digite o nome do cargo: ')
    sql_insert_cargo = f'''INSERT INTO tb_cargo
                    (nome)
                    VALUES('{v_nome_cargo}')'''
    cursor.execute(sql_insert_cargo)
    conexao.commit()

def insert_empregado():
    v_nome_empregado = input('Digite o nome do empregado: ')
    v_data_nascimento_empregado = input('Digite o data de nascimento do empregado: ')
    v_genero_empregado = input('Digite o genero do empregado: ')
    v_cod_cargo_empregado = input('Digite o codigo do cargo: ')
    sql_insert_empregado = f'''INSERT INTO tb_empregado
                        (nome, data_nascimento, genero, cod_cargo)
                        VALUES('{v_nome_empregado}', '{v_data_nascimento_empregado}','{v_genero_empregado}',{v_cod_cargo_empregado})'''
    cursor.execute(sql_insert_empregado)
    conexao.commit()

def join():
    print('- Consulta:')
    sql_join = '''select c.identificador, c.nome, e.identificador, e.nome, e.data_nascimento, e.genero, e.cod_cargo
                from tb_cargo c join tb_empregado e
                where e.cod_cargo = c.identificador'''
    cursor.execute(sql_join)
    l_registros = cursor.fetchall()
    print('- List of tuplas')
    print(l_registros)
    print('- Tuplas')
    for record in l_registros:
     print(record)
    print('Colunas, notação de vetor:')
    for record in l_registros:
        print('Identificador cargo:', record[0])
        print('Cargo:', record[1])
        print('Identificador empregado:', record[2])
        print('Nome:', record[3])
        print('Data de nascimento:', record[4])
        print('Genero:', record[5])
        print('Codigo cargo:', record[6])

    print('Quantidade de registros na tabela (rowcount):', cursor.rowcount)

def select_all_tb_cargo():
     print('- Consulta:')
     sql_select_cargo = f'SELECT * FROM tb_cargo'
     cursor.execute(sql_select_cargo)
     l_registros = cursor.fetchall()
     print('- List of tuplas')
     print(l_registros)
     print('- Tuplas')
     for record in l_registros:
        print(record)
     print('Colunas, notação de vetor:')
     for record in l_registros:
         print('Identificador:', record[0])
         print('Nome:', record[1])
     print('Quantidade de registros na tabela (rowcount):', cursor.rowcount)

def select_all_tb_empregado():
     print('- Consulta:')
     sql_select_empregado = f'SELECT * FROM tb_empregado'
     cursor.execute(sql_select_empregado)
     l_registros = cursor.fetchall()
     print('- List of tuplas')
     print(l_registros)
     print('- Tuplas')
     for record in l_registros:
         print(record)
     print('Colunas, notação de vetor:')
     for record in l_registros:
         print('Identificador:', record[0])
         print('Nome:', record[1])
         print('Data de nascimento:', record[2])
         print('Genero:', record[3])
         print('Codigo do cargo:', record[4])
     print('Quantidade de registros na tabela (rowcount):', cursor.rowcount)

def delete_cargo():
    pesquisa = input('Digite o identificador do cargo: ')
    sql_delete = f'''delete from tb_cargo where identificador= {pesquisa}'''
    cursor.execute(sql_delete)
    conexao.commit()
    print('Registros apagados: ', cursor.rowcount)

def delete_empregado():
    pesquisa = input('Digite o nome do empregado: ')
    sql_delete = f'''delete from tb_empregado
                where nome = '{pesquisa}' '''
    cursor.execute(sql_delete)
    conexao.commit()
    print('Registros apagados: ', cursor.rowcount)

def update_cargo():
    novo_valor = input('Digite o novo nome do cargo: ')
    pesquisa = input('Digite o nome do cargo: ')
    sql_update = f'''update tb_cargo
                set nome = '{novo_valor}'
                where nome = '{pesquisa}' '''
    cursor.execute(sql_update)
    conexao.commit()
    print('Registros atualizados: ', cursor.rowcount)

def update_empregado():
    pesquisa = input('Digite o nome do empregado: ')
    novo_valor = input('Digite a nova data de nascimento: ')
    sql_update = f'''update tb_empregado
                set data_nascimento = '{novo_valor}'
                where nome = '{pesquisa}' '''
    cursor.execute(sql_update)
    conexao.commit()
    print('Registros atualizados: ', cursor.rowcount)

def show_records_cargo():
    print('- Consulta:')
    sql_show_cargo = f'SELECT * FROM tb_cargo'
    cursor.execute(sql_show_cargo)
    l_registros = cursor.fetchall()
    for record in l_registros:
        print('Identificador:', record[0])
        print('Nome:', record[1])
    print('Quantidade de registros na tabela (rowcount):', cursor.rowcount)

def close_connection():
    conexao.close()
    cursor.close()

if __name__ == '__main__':
    conexao = create_connection()
    cursor = conexao.cursor()
    create_database()
    # create_table()
    # input_crud()
    while True:
        menu = input('[c] Create, [i] Insert, [r] Select, [j] Join [d] Delete, [u] Update, [s] para sair:')
        if menu == 'c':
            create_table()
        elif menu == 'i':
            sub_menu = input('[c] Cargo - [e] Empregado: ')
            if sub_menu == 'c':
                insert_cargo()
                show_records_cargo()
            elif sub_menu == 'e':
                insert_empregado()
        elif menu == 'e':
            insert_empregado()
        elif menu == 'r':
            sub_menu = input('[c] Cargo - [e] Empregado: ')
            if sub_menu == 'c':
                select_all_tb_cargo()
            elif sub_menu == 'e':
                select_all_tb_empregado()
        elif menu == 'j':
                join()
        elif menu == 'd':
            sub_menu = input('[c] Cargo - [e] Empregado: ')
            if sub_menu == 'c':
                delete_cargo()
                show_records_cargo()
            elif sub_menu == 'e':
                delete_empregado()
        elif menu == 'u':
            sub_menu = input('[c] Cargo - [e] Empregado: ')
            if sub_menu == 'c':
                update_cargo()
                show_records_cargo()
            elif sub_menu == 'e':
                update_empregado()
        elif menu == 's':
            close_connection()
            break
        else:
            print('Comando desconhecido')
