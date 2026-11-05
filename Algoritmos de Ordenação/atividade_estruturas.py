
dados = []
tipo_atual = None
capacidade = 0
inicio = 0
fim = 0
quantidade = 0


# Selecionar estrutura
def selecionar_tipo(novo_tipo):
    global tipo_atual, dados, capacidade
    global inicio, fim, quantidade

    if tipo_atual != novo_tipo:
        tipo_atual = novo_tipo
        dados = []
        capacidade = 0
        inicio = 0
        fim = 0
        quantidade = 0


# Obter valores da estrutura
def obter_valores():
    if tipo_atual == "Fila Circular":
        valores = []

        for i in range(quantidade):
            posicao = (inicio + i) % capacidade
            valores.append(dados[posicao])

        return valores

    return dados.copy()


# Atualizar valores depois da ordenacao
def atualizar_valores(valores):
    global dados, inicio, fim, quantidade

    if tipo_atual == "Fila Circular":
        dados = [None] * capacidade
        quantidade = len(valores)
        inicio = 0
        fim = quantidade % capacidade

        for i in range(quantidade):
            dados[i] = valores[i]
    else:
        dados = valores.copy()


# Criar estrutura
def criar_estrutura():
    global dados, capacidade, inicio, fim, quantidade

    try:
        tamanho = int(input("Digite o tamanho da estrutura: "))

        if tamanho <= 0:
            print("O tamanho deve ser maior que zero!")
            return

        capacidade = tamanho

        if tipo_atual == "Fila Circular":
            dados = [None] * capacidade
            inicio = 0
            fim = 0
            quantidade = 0
        else:
            dados = []

        print(tipo_atual, "criada com sucesso!")

    except ValueError:
        print("Digite um numero inteiro valido!")


# Armazenar valor
def armazenar_valor():
    global fim, quantidade

    if capacidade == 0:
        print("Crie a estrutura primeiro!")
        return

    if tipo_atual == "Fila Circular":
        if quantidade == capacidade:
            print("Fila circular cheia!")
            return

    elif len(dados) >= capacidade:
        print("Estrutura cheia!")
        return

    try:
        valor = int(input("Digite o valor: "))

        if tipo_atual == "Fila Circular":
            dados[fim] = valor
            fim = (fim + 1) % capacidade
            quantidade += 1
        else:
            dados.append(valor)

        print("Valor armazenado com sucesso!")

    except ValueError:
        print("Digite um numero inteiro valido!")


# Extrair valor
def extrair_valor():
    global inicio, quantidade

    if capacidade == 0:
        print("Crie a estrutura primeiro!")
        return

    if tipo_atual == "Fila Circular":
        if quantidade == 0:
            print("Fila circular vazia!")
            return

        valor = dados[inicio]
        dados[inicio] = None
        inicio = (inicio + 1) % capacidade
        quantidade -= 1

    elif len(dados) == 0:
        print("Estrutura vazia!")
        return

    elif tipo_atual == "Pilha":
        valor = dados.pop()

    else:
        valor = dados.pop(0)

    print("Valor extraido:", valor)


# Imprimir conteudo
def imprimir_conteudo():
    if capacidade == 0:
        print("Crie a estrutura primeiro!")
        return

    print("Conteudo:", obter_valores())


# Bubble Sort
def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


# Selection Sort
def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        menor = i

        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]


# Insertion Sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave


# Menu de ordenacao
def menu_ordenar():
    if tipo_atual is None or capacidade == 0:
        print("\nCrie primeiro uma estrutura!")
        return

    while True:
        print("\n===== MENU ORDENAR =====")
        print("1 - Bubble Sort")
        print("2 - Selection Sort")
        print("3 - Insertion Sort")
        print("4 - Voltar ao menu anterior")

        opcao = input("Escolha uma opcao: ")

        if opcao in ["1", "2", "3"]:
            lista = obter_valores()

            if opcao == "1":
                bubble_sort(lista)
                print("Bubble Sort realizado!")

            elif opcao == "2":
                selection_sort(lista)
                print("Selection Sort realizado!")

            elif opcao == "3":
                insertion_sort(lista)
                print("Insertion Sort realizado!")

            atualizar_valores(lista)
            print("Resultado:", obter_valores())

        elif opcao == "4":
            break

        else:
            print("Opcao invalida!")


# Menu das estruturas
def menu_estrutura():
    while True:
        print("\n===== MENU", tipo_atual.upper(), "=====")
        print("1 - Criar estrutura")
        print("2 - Armazenar valor")
        print("3 - Extrair valor")
        print("4 - Imprimir conteudo")
        print("5 - Voltar ao menu anterior")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            criar_estrutura()

        elif opcao == "2":
            armazenar_valor()

        elif opcao == "3":
            extrair_valor()

        elif opcao == "4":
            imprimir_conteudo()

        elif opcao == "5":
            break

        else:
            print("Opcao invalida!")


# Menu principal
while True:
    print("\n========== MENU PRINCIPAL ==========")
    print("1 - PILHA")
    print("2 - FILA")
    print("3 - FILA CIRCULAR")
    print("4 - ORDENAR")
    print("5 - SAIR")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        selecionar_tipo("Pilha")
        menu_estrutura()

    elif opcao == "2":
        selecionar_tipo("Fila")
        menu_estrutura()

    elif opcao == "3":
        selecionar_tipo("Fila Circular")
        menu_estrutura()

    elif opcao == "4":
        menu_ordenar()

    elif opcao == "5":
        print("Programa encerrado!")
        break

    else:
        print("Opcao invalida!")
