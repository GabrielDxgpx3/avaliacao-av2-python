from Util.Entrada import Entrada
from Util.Tela import Tela
from Aluno import Aluno
from time import sleep

class Menu:

	def __init__(self):
		self.OPC_LIVROS = 1
		self.OPC_ALUNOS = 2
		self.OPC_SOBRE = 3
		self.OPC_SAIR = 4

		self.OPC_CADASTRAR_ALUNO = 1
		self.OPC_LISTAR_ALUNOS = 2
		self.OPC_ATUALIZAR_ALUNO = 3
		self.OPC_DELETAR_ALUNO = 4
		self.OPC_VOLTAR = 5

		self.tela = Tela()
		self.entrada = Entrada()
		self.aluno = Aluno()

	def menuPrincipal(self):
		self.tela.home()
		self.tela.menu()

		while True:
			opcao_escolhida = self.entrada.lerOpcaoMenu()

			if opcao_escolhida == self.OPC_LIVROS:
				self.menuLivros()
			elif opcao_escolhida == self.OPC_ALUNOS:
				self.menuAlunos()
			elif opcao_escolhida == self.OPC_SOBRE:
				self.menuSobre()
			elif opcao_escolhida == self.OPC_SAIR:
				self.menuSair()
				break;
			else:
				self.tela.opcaoInvalida()


	def menuAlunos(self):
		self.tela.alunos()

		while True:
			opcao_escolhida = self.entrada.lerOpcaoMenu()

			if opcao_escolhida == self.OPC_CADASTRAR_ALUNO:
				self.menuCadastrarAluno()
			elif opcao_escolhida == self.OPC_LISTAR_ALUNOS:
				self.menuListarAlunos()
			elif opcao_escolhida == self.OPC_ATUALIZAR_ALUNO:
				self.menuAtulizarAluno()
			elif opcao_escolhida == self.OPC_DELETAR_ALUNO:
				self.menuDeletarAluno()
			elif opcao_escolhida == self.OPC_VOLTAR:
				self.irParaMenuPrincipal()
				break;
			else:
				self.tela.opcaoInvalida()


	def menuCadastrarAluno(self):
		self.aluno.processarCadastro()
		sleep(1)
		self.tela.limpar()
		self.tela.alunos()

	def menuListarAlunos(self):
		self.tela.limpar()
		self.aluno.listarAlunos()

		while True:
			self.entrada.precioneParaVoltarMenu()
			self.irParaMenuAluno()
			break

	def menuAtulizarAluno(self):
		self.tela.limpar()
		self.aluno.listarAlunos()

		while True:
			self.aluno.processarAtualizacao(self.entrada.lerIdAluno('para atualizar'))
			sleep(1)
			self.tela.limpar()
			self.tela.alunos()
			break;

	def menuDeletarAluno(self):
		self.tela.limpar()
		self.aluno.listarAlunos()

		while True:
			self.aluno.processarExclusao(self.entrada.lerIdAluno('para excluir'))
			sleep(1)
			self.tela.limpar()
			self.tela.alunos()
			break;


	def menuLivros(self):
		print("menu livros")

	def menuSobre(self):
		self.tela.sobre()

		while True:
			self.entrada.precioneParaVoltarMenu()
			self.irParaMenuPrincipal()
			break;

	def menuSair(self):
		self.tela.sair()

	def irParaMenuAluno(self):
		self.tela.limpar()
		self.tela.alunos()

	def irParaMenuPrincipal(self):
		self.tela.limpar()
		self.tela.home()
		self.tela.menu()
