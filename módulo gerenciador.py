from operator import itemgetter
from tarefa import Tarefa
from datetime import datetime

class Gerenciador():
    '''Classe que irá gerenciar a lista de tarefas do usuário'''  
    tarefas = []
    '''Lista que receberá as tarefas do usuário'''
    
    def __init__(self):
        pass
    

    def listar_tarefas(self):
        '''Método que organizará por data e listará as tarefas a serem realizadas'''
        if len(Gerenciador.tarefas) > 0:
            Gerenciador.tarefas.sort(key=itemgetter(2))
            n = 0
            print('Listar Tarefas')
            for i in Gerenciador.tarefas:
                n+=1
                print(f'{n} - {i[0]} - {i[1]} - {i[2]}')

        else:
            print('A lista de tarefas está vazia.')
            print('Coisa boa! Aproveite o dia!')
    
    def adicionar_tarefa(self):
        '''Método adicionará novas tarefas na lista de tarefas'''
        tarefa = input("Informe a tarefa a ser realizada: ")
        data_limite = input('Infome até que data (d/m/aaaa) essa tarefa deve ser realizada. Se for hoje, digite a data de hoje. \n Caso não haja uma data limite, digite 0: ')
        Tarefa(tarefa, data_limite)
        if data_limite != '0':
            data_limite = datetime.strptime(data_limite, '%d/%m/%Y').date()
            Gerenciador.tarefas.append(['[ ]', tarefa, (f"Data limite para realização: {datetime.strftime(data_limite, '%d/%m/%Y')}")])
            with open('lista_de_tarefas.txt', 'a', encoding='utf-8') as arquivo_txt:
                arquivo_txt.write(f"[ ] - {tarefa} - Data limite para realização: {datetime.strftime(data_limite, '%d/%m/%Y')}\n")
                arquivo_txt.close()
        else:
            Gerenciador.tarefas.append(['[ ]', tarefa, 'sem prazo estabelecido para realização'])
            with open('lista_de_tarefas.txt', 'a', encoding='utf-8') as arquivo_txt:
                arquivo_txt.write(f'[ ] - {tarefa} - sem prazo estabelecido para realização\n')
                arquivo_txt.close()
    
    def marcar_como_concluida(self):
        '''Método que marcará as tarefas como concluída na lista de tarefas'''
        if len(Gerenciador.tarefas) > 0:
            print('Das seguintes tarefas:')
            Gerenciador().listar_tarefas()
            marcar = int(input('Qual tarefa você quer marcar como concluída: '))
            tarefa_concluida = ['[x]', Gerenciador.tarefas[marcar-1][1], Gerenciador.tarefas[marcar-1][2]]
            with open('lista_de_tarefas.txt', 'a', encoding='utf-8') as arquivo_txt:
                arquivo_txt.write(f'[x] - {Gerenciador.tarefas[marcar-1][1]}\n')
                arquivo_txt.close()
            del Gerenciador.tarefas[marcar-1]
            Gerenciador.tarefas.append(tarefa_concluida)
            
        else:
            print('A lista de tarefas está vazia')