class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade  = idade
class Aluno(Pessoa):
    def __init__(self, nome, idade, id_aluno):
        super().__init__(nome, idade)
        self.id_aluno = id_aluno
    def exibir_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | ID do Aluno: {self.id_aluno}")

alunos = [
    Aluno("Angelo", 18, 1),
    Aluno("João", 16, 2)
]

for aluno in alunos:
    aluno.exibir_dados()
