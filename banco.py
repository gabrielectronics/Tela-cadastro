import sqlite3

conexao = sqlite3.connect('nuberUm.db')
cursor = conexao.cursor()
cursor.execute('DROP TABLE IF EXISTS testeTabela')
cursor.execute('CREATE TABLE testeTabela'
            '(Matricula INTEGER PRIMARY KEY , Nome TEXT, Documento INTEGER)')

conexao.close()