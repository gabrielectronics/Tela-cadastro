import sqlite3

def insereDado(nome, numeroDoc, matricula):
    cur.execute("INSERT INTO testeTabela (Nome, Documento, Matricula) VALUES('{}','{}','{}')".format(nome, numeroDoc, matricula))
    conexao.commit()
    
def deletaDado(matricula):
    cur.execute('DELETE FROM testeTabela WHERE Matricula = "{}"'.format(matricula))
    conexao.commit()

def atualizaDado(matricula, nome, numDoc):
    cur.execute("UPDATE testeTabela SET Nome = '{}', Documento = '{}' WHERE Matricula = '{}'".format(matricula, nome, numDoc))
    conexao.commit()

def selecionaDado(doc):
    cur.execute("SELECT * FROM testeTabela WHERE Documento = '{}'".format(doc))
    print(cur.fetchone())


conexao = sqlite3.connect('nuberUm.db')
conexao.commit()
cur = conexao.cursor()
