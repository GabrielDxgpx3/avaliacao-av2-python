from Util.Crud import Crud 
from Util.Tela import Tela
from Util.Entrada import Entrada

class Aluno:

	def __init__(self):
		self.crud = Crud()
		self.entrada = Entrada()
		self.tela = Tela()

		self.tabela = "aluno"

	def novoAluno(self, nome, ra):
		return self.crud.create(self.tabela).fields(["nome", "ra"]).values([nome, ra]).executar()

	def selectAlunos(self):
		return self.crud.select(["id", "nome", "ra"]).de(self.tabela).executar()

	def deletarAluno(self, idAluno):
		return self.crud.delete().de(self.tabela).onde("id").igualA(str(idAluno)).executar()

	def atualizarAluno(self, nome, ra, idAluno):
		return self.crud.update(self.tabela).set(['nome', 'ra'], [nome, ra]).onde("id").igualA(str(idAluno)).executar()

	def listarAlunos(self):
		tela = Tela()
		alunos = self.selectAlunos()

		tela.listarAlunos()

		for aluno in alunos:
			print(self.formatarAluno(aluno))
			tela.linha()

		
	def formatarAluno(self, aluno):
		return "{} - {}, {}".format(aluno['id'], aluno['nome'], aluno['ra'])

	def processarCadastro(self):
		self.tela.limpar()
		self.tela.cadastroAluno()
		nome = self.entrada.lerNomeAluno()
		ra = self.entrada.lerRaAluno()

		try:
			self.novoAluno(nome, ra)
		except Exception as e:
			self.tela.erroCadastrarAluno()
			return

		self.tela.sucessoCadastrarAluno()

	def processarAtualizacao(self, idAluno):
		self.tela.limpar()
		self.tela.atualizarAluno()
		nome = self.entrada.lerNomeAluno()
		ra = self.entrada.lerRaAluno()

		try:
			self.atualizarAluno(nome, ra, idAluno)
		except Exception as e:
			self.tela.erroAtualizarAluno()
			return

		self.tela.sucessoAtualizarAluno()

	def processarExclusao(self, idAluno):
		self.tela.limpar()
		self.tela.excluirAluno()

		try:
			self.deletarAluno(idAluno)
		except Exception as e:
			self.tela.erroExcluirAluno()
			return

		self.tela.sucessoExcluirAluno()




