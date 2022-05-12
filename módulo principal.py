from gerenciador import Gerenciador
from time import sleep

continuar = True
while continuar:
    print("O que deseja fazer?")
    print("1 - Exibir a lista de tarefas")
    print("2 - Adicionar uma nova tarefa")
    print("3 - Marcar uma tarefa como concluída")
    print("4 - Sair")
    opcao = int(input("> "))
    if opcao == 1:
        Gerenciador().listar_tarefas()
    elif opcao == 2:
        Gerenciador().adicionar_tarefa()
    elif opcao == 3:
        Gerenciador().marcar_como_concluida()
    elif opcao == 4:
        print("Fechando Lista de Tarefas...")
        sleep(1)
        print('Até breve!')
        continuar = False