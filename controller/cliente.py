#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(id, nome, endereco, telefone):
    db.cur.execute("""
                   INSERT into public.tbcliente ( id, nome, endereço, telefone)
                   VALUES ('%s','%s','%s','%s')
                   """ % (id, nome, endereco, telefone))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM tbcliente
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows
#função para excluir registros no banco de dados
def deletar(id):
    db.cur.execute("""
              DELETE FROM tbcliente WHERE id = '%s'
    """ % (id))
    db.con.commit()
            
