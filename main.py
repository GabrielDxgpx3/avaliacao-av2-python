from Crud import Crud

#print(str('m'.join(['a', 'b'])) )
crud = Crud()
#crud.create("pessoa").fields(['nome', 'idade']).values(["Gabriel", "23"]);
#crud.update("pessoa").set(['nome', 'idade'], ["Gabriel", "23"])
crud.select(['nome', 'id']).de('pessoa').join("endereco").on("pessoa.id").igualA("endereco.id_pessoa").e("endereco.id").igualA("casa.id").onde("pessoa.nome").pareceCom("'asd'")
print(crud.getSQL());
#conexao.disconnect()