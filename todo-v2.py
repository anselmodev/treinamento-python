from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possível IndexError
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (concluída)' if self.feito else '')


def main():
    casa = Projeto('Casa de Tarefas')
    casa.add('Passar Roupa')
    casa.add('Lavar Prato')
    print(casa)

    casa.procurar('Lavar Prato').concluir()
    for tarefa in casa.tarefas:
        print(f'- {tarefa}')
    print(casa)


if __name__ == '__main__':
    main()
