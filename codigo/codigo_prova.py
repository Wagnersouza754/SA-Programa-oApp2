
# ==========================================================
# PROJETO: APLICATIVO DE TRANSPORTE
# Tema: Aplicativo de transporte inspirado no Uber
#
# A ideia deste projeto é criar um aplicativo onde as pessoas
# possam se cadastrar, escolher um tipo de transporte,
# encontrar um motorista e saber quanto vai custar a viagem.
#
# O programa também permite consultar as corridas que já
# foram solicitadas e visualizar as informações dos motoristas.
# ==========================================================


# Classe responsável por guardar as informações dos motoristas
# Cada motorista terá seus dados pessoais e as informações do veículo
import os
os.system("cls")
class Motorista:

    def __init__(self, nome, placa, tipo_carro, idade, marca,
                 modelo, cor, ano, avaliacao, viagens, telefone):

        self.nome = nome
        self.placa = placa
        self.tipo_carro = tipo_carro
        self.idade = idade
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.avaliacao = avaliacao
        self.viagens = viagens
        self.telefone = telefone

        # Quando o motorista é cadastrado, ele começa disponível
        # para receber uma nova solicitação de corrida
        self.disponivel = True


# Classe que guarda as informações de cada passageiro
# Por enquanto, utilizamos o nome e o CPF para identificar a pessoa
class Passageiro:

    def __init__(self, nome, cpf):

        self.nome = nome
        self.cpf = cpf


# Classe responsável por organizar as corridas e calcular os preços
# Aqui ficam as informações de cada viagem solicitada
class Corrida:

    def __init__(self, passageiro, motorista, origem, destino,
                 distancia, pagamento, quantidade_passageiros):

        self.passageiro = passageiro
        self.motorista = motorista
        self.origem = origem
        self.destino = destino
        self.distancia = distancia
        self.pagamento = pagamento
        self.quantidade_passageiros = quantidade_passageiros

        self.valor = 0

        # Assim que uma corrida é criada, o programa já calcula seu valor
        self.calcular_preco()

    def calcular_preco(self):

        # Cada tipo de transporte possui um valor inicial
        # e um preço diferente para cada quilômetro percorrido

        if self.motorista.tipo_carro == "MOTO":

            bandeirada = 3.00
            preco_km = 1.20

        elif self.motorista.tipo_carro == "TAXI":

            bandeirada = 6.00
            preco_km = 2.50

        elif self.motorista.tipo_carro == "ECONOMY":

            bandeirada = 5.00
            preco_km = 1.50

        elif self.motorista.tipo_carro == "COMFORT":

            bandeirada = 5.00
            preco_km = 2.20

        else:

            bandeirada = 5.00
            preco_km = 3.50

        # Soma a bandeirada com o valor dos quilômetros percorridos
        # Assim chegamos ao preço total que o passageiro deverá pagar
        self.valor = bandeirada + (self.distancia * preco_km)


# Essas listas guardam os dados cadastrados durante a utilização
# do aplicativo. Quando o programa é fechado, os dados são perdidos.

lista_motoristas = []
lista_passageiros = []
lista_corridas = []


# ----------------------------------------------------------
# CADASTRO DE MOTORISTA
# ----------------------------------------------------------
# Essa função permite que um novo motorista entre no aplicativo
# e informe seus dados pessoais e as características do veículo
def cadastrar_motorista():

    print("\n===== CADASTRO DE MOTORISTA =====")

    nome = input("Digite o nome do motorista: ")

    # Não adianta cadastrar um nome muito curto ou deixar o campo vazio
    if len(nome.strip()) < 3:

        print("Nome inválido! Digite pelo menos 3 letras.")
        return

    # Pedimos a idade para completar as informações do motorista
    try:

        idade = int(input("Digite a idade do motorista: "))

        # O motorista precisa ser maior de idade para continuar
        if idade < 18 or idade > 100:

            print("Idade inválida! É necessário ter pelo menos 18 anos.")
            return

    except ValueError:

        print("Ops! Digite uma idade usando apenas números.")
        return

    telefone = input("Digite o telefone para contato: ").strip()

    placa = input("Digite a placa do veículo: ").strip().upper()

    # Antes de continuar, verificamos se outro motorista já
    # cadastrou um veículo com a mesma placa
    for motorista in lista_motoristas:

        if motorista.placa == placa:

            print("Essa placa já está cadastrada no aplicativo!")
            return

    # Agora vamos conhecer um pouco mais sobre o veículo
    print("\n===== DADOS DO VEÍCULO =====")

    marca = input("Qual é a marca do veículo? ").strip()
    modelo = input("Qual é o modelo do veículo? ").strip()
    cor = input("Qual é a cor do veículo? ").strip()

    try:

        ano = int(input("Qual é o ano do veículo? "))

        # Verificamos se o ano informado está dentro do intervalo aceito
        if ano < 1900 or ano > 2026:

            print("Ano inválido! Confira o ano do veículo.")
            return

    except ValueError:

        print("Digite um ano válido usando apenas números.")
        return

    # O motorista escolhe qual tipo de transporte deseja oferecer
    print("\n===== ESCOLHA A MODALIDADE DE TRANSPORTE =====")

    print("1 - Uber Moto")
    print("2 - Uber Taxi")
    print("3 - Economy / UberX")
    print("4 - Comfort")
    print("5 - Black")

    # Cada número representa uma modalidade disponível no aplicativo
    categorias = {
        "1": "MOTO",
        "2": "TAXI",
        "3": "ECONOMY",
        "4": "COMFORT",
        "5": "BLACK"
    }

    tipo = input("\nQual modalidade deseja oferecer? ").strip()

    # Se o motorista escolher uma opção que não existe, o cadastro para
    if tipo not in categorias:

        print("Essa modalidade não existe. Tente novamente.")
        return

    tipo = categorias[tipo]

    # Também guardamos algumas informações sobre a experiência do motorista
    print("\n===== INFORMAÇÕES DO MOTORISTA =====")

    try:

        avaliacao = float(input("Qual é a nota do motorista (0 a 5)? "))

        # A avaliação não pode ser menor que zero nem maior que cinco
        if avaliacao < 0 or avaliacao > 5:

            print("A nota precisa estar entre 0 e 5.")
            return

        viagens = int(input("Quantas viagens ele já realizou? "))

        if viagens < 0:

            print("A quantidade de viagens não pode ser negativa.")
            return

    except ValueError:

        print("Confira as informações e digite valores válidos.")
        return

    # Com todas as informações preenchidas, criamos o cadastro do motorista
    novo_motorista = Motorista(
        nome, placa, tipo, idade, marca, modelo,
        cor, ano, avaliacao, viagens, telefone
    )

    # Guardamos o novo motorista para que ele possa aparecer
    # quando algum passageiro estiver procurando uma corrida
    lista_motoristas.append(novo_motorista)

    print("\nCadastro realizado com sucesso!")
    print("Agora o motorista já faz parte do nosso aplicativo!")


# ----------------------------------------------------------
# CADASTRO DE PASSAGEIRO
# ----------------------------------------------------------
# Aqui o passageiro informa seus dados para poder utilizar o aplicativo
def cadastrar_passageiro():

    print("\n===== CADASTRO DE PASSAGEIRO =====")

    nome = input("Digite o nome do passageiro: ")

    # Conferimos se o nome foi preenchido corretamente
    if len(nome.strip()) < 3:

        print("Nome inválido! Digite pelo menos 3 letras.")
        return

    cpf = input("Digite o CPF (somente números): ").strip()

    # Para este projeto, estamos considerando um CPF com 11 números
    if len(cpf) != 11 or not cpf.isdigit():

        print("CPF inválido! Digite os 11 números corretamente.")
        return

    # Evitamos que a mesma pessoa seja cadastrada mais de uma vez
    for passageiro in lista_passageiros:

        if passageiro.cpf == cpf:

            print("Esse CPF já possui um cadastro!")
            return

    # Depois de conferir os dados, criamos o cadastro do passageiro
    novo_passageiro = Passageiro(nome, cpf)

    lista_passageiros.append(novo_passageiro)

    print("\nPassageiro cadastrado com sucesso!")
    print("Você já pode solicitar uma corrida!")


# ----------------------------------------------------------
# INFORMAÇÕES DO MOTORISTA
# ----------------------------------------------------------
# Essa função mostra ao passageiro quem será o motorista
# e qual veículo será utilizado na viagem
def mostrar_motorista(motorista):

    print("\n================================")
    print("       DADOS DO MOTORISTA")
    print("================================")

    print("\n===== PERFIL DO MOTORISTA =====")

    print("Nome:", motorista.nome)
    print("Idade:", motorista.idade, "anos")
    print("Telefone:", motorista.telefone)
    print("Avaliação:", motorista.avaliacao, "de 5 estrelas")
    print("Viagens realizadas:", motorista.viagens)

    print("\n===== INFORMAÇÕES DO VEÍCULO =====")

    print("Marca:", motorista.marca)
    print("Modelo:", motorista.modelo)
    print("Cor:", motorista.cor)
    print("Ano:", motorista.ano)
    print("Placa:", motorista.placa)

    # Mostramos o nome da modalidade de uma maneira mais fácil de entender
    nomes_modalidades = {
        "MOTO": "Uber Moto",
        "TAXI": "Uber Taxi",
        "ECONOMY": "Economy / UberX",
        "COMFORT": "Uber Comfort",
        "BLACK": "Uber Black"
    }

    print("Modalidade:", nomes_modalidades.get(motorista.tipo_carro))

    print("\n===== PREVISÃO DE CHEGADA =====")

    # Como ainda não temos GPS, usamos um tempo de chegada ilustrativo
    tempo_chegada = 5

    print("Seu motorista está a caminho!")
    print("Previsão de chegada:", tempo_chegada, "minutos")


# ----------------------------------------------------------
# SOLICITAÇÃO DE CORRIDA
# ----------------------------------------------------------
# Essa é uma das partes principais do aplicativo.
# É aqui que o passageiro escolhe o trajeto, a modalidade,
# o motorista e a forma de pagamento.
def pedir_corrida():

    print("\n===== SOLICITAR UMA CORRIDA =====")

    # Primeiro precisamos verificar se já existem passageiros cadastrados
    if len(lista_passageiros) == 0:

        print("Ainda não temos passageiros cadastrados.")
        print("Faça seu cadastro antes de solicitar uma corrida.")
        return

    # Também precisamos ter pelo menos um motorista cadastrado
    if len(lista_motoristas) == 0:

        print("Ainda não temos motoristas cadastrados.")
        print("Volte quando tivermos motoristas disponíveis.")
        return

    cpf = input("Digite o CPF do passageiro: ").strip()

    # Procuramos o passageiro pelo CPF informado
    passageiro_encontrado = None

    for passageiro in lista_passageiros:

        if passageiro.cpf == cpf:

            passageiro_encontrado = passageiro
            break

    # Se não encontrar o CPF, não será possível continuar
    if passageiro_encontrado == None:

        print("Não encontramos um passageiro com esse CPF.")
        return

    print("\nOlá,", passageiro_encontrado.nome + "!")

    # Agora precisamos saber de onde o passageiro vai sair
    # e para qual lugar deseja ir
    origem = input("Qual será o local de saída? ").strip()
    destino = input("Qual será o destino da viagem? ").strip()

    # Os dois locais precisam estar preenchidos
    if origem == "" or destino == "":

        print("Informe corretamente o local de saída e o destino.")
        return

    # O passageiro informa a distância aproximada da viagem
    try:

        distancia = float(input("Qual é a distância da viagem em KM? "))

        if distancia <= 0:

            print("A distância precisa ser maior que zero.")
            return

    except ValueError:

        print("Distância inválida! Exemplo de valor correto: 8.5")
        return

    # Mostramos as opções de transporte disponíveis no aplicativo
    print("\n===== QUAL TRANSPORTE VOCÊ DESEJA? =====")

    print("1 - Uber Moto")
    print("2 - Uber Taxi")
    print("3 - Economy / UberX")
    print("4 - Comfort")
    print("5 - Black")

    categorias = {
        "1": "MOTO",
        "2": "TAXI",
        "3": "ECONOMY",
        "4": "COMFORT",
        "5": "BLACK"
    }

    tipo = input("\nEscolha uma modalidade: ").strip()

    # Conferimos se a modalidade escolhida está disponível
    if tipo not in categorias:

        print("Opção inválida! Escolha uma modalidade disponível.")
        return

    tipo = categorias[tipo]

    # Perguntamos quantas pessoas vão utilizar o transporte
    try:

        quantidade_passageiros = int(
            input("Quantas pessoas vão viajar? ")
        )

        if quantidade_passageiros < 1:

            print("É necessário informar pelo menos um passageiro.")
            return

        # Na modalidade de moto, consideramos apenas um passageiro
        if tipo == "MOTO" and quantidade_passageiros > 1:

            print("Na modalidade Uber Moto é permitido apenas um passageiro.")
            return

        # Nas outras modalidades, consideramos até quatro passageiros
        if tipo != "MOTO" and quantidade_passageiros > 4:

            print("Essa modalidade permite até quatro passageiros.")
            return

    except ValueError:

        print("Digite uma quantidade válida de passageiros.")
        return

    # Procuramos somente os motoristas que oferecem a modalidade
    # escolhida e que ainda estão livres para receber uma corrida
    motoristas_disponiveis = []

    for motorista in lista_motoristas:

        if motorista.tipo_carro == tipo and motorista.disponivel == True:

            motoristas_disponiveis.append(motorista)

    # Se ninguém estiver disponível, avisamos o passageiro
    if len(motoristas_disponiveis) == 0:

        print("No momento não encontramos motoristas disponíveis.")
        print("Tente escolher outra modalidade ou tente novamente depois.")
        return

    # Mostramos os motoristas que podem realizar a viagem
    print("\n===== MOTORISTAS DISPONÍVEIS =====")

    for i, motorista in enumerate(motoristas_disponiveis):

        print("\nOpção:", i + 1)
        print("Motorista:", motorista.nome)
        print("Veículo:", motorista.marca, motorista.modelo)
        print("Cor:", motorista.cor)
        print("Placa:", motorista.placa)
        print("Avaliação:", motorista.avaliacao, "estrelas")

    # O passageiro escolhe quem deseja que faça sua corrida
    try:

        escolha = int(input("\nDigite o número do motorista escolhido: "))

        if escolha < 1 or escolha > len(motoristas_disponiveis):

            print("Essa opção não existe. Escolha um motorista da lista.")
            return

    except ValueError:

        print("Digite um número válido.")
        return

    # Guardamos o motorista escolhido para utilizar durante a solicitação
    motorista_encontrado = motoristas_disponiveis[escolha - 1]

    # Antes de confirmar, mostramos todas as informações do motorista
    mostrar_motorista(motorista_encontrado)

    # Criamos uma corrida provisória para descobrir o preço
    # O cadastro definitivo só acontece depois da confirmação
    corrida_provisoria = Corrida(
        passageiro_encontrado,
        motorista_encontrado,
        origem,
        destino,
        distancia,
        "",
        quantidade_passageiros
    )

    print("\n===== RESUMO DA SUA VIAGEM =====")

    print("Passageiro:", passageiro_encontrado.nome)
    print("Local de saída:", origem)
    print("Destino:", destino)
    print("Distância:", distancia, "KM")
    print("Modalidade:", tipo)
    print("Quantidade de passageiros:", quantidade_passageiros)

    print("Valor estimado: R$",
          round(corrida_provisoria.valor, 2))

    # Agora o passageiro escolhe como pretende pagar pela corrida
    print("\n===== COMO DESEJA PAGAR? =====")

    print("1 - Dinheiro")
    print("2 - PIX")
    print("3 - Cartão de crédito")
    print("4 - Cartão de débito")

    pagamento = input("Escolha a forma de pagamento: ")

    # Cada opção representa uma forma de pagamento
    formas_pagamento = {
        "1": "Dinheiro",
        "2": "PIX",
        "3": "Cartão de crédito",
        "4": "Cartão de débito"
    }

    # Verificamos se o passageiro escolheu uma opção válida
    if pagamento not in formas_pagamento:

        print("Forma de pagamento inválida. Tente novamente.")
        return

    pagamento = formas_pagamento[pagamento]

    # Antes de finalizar, mostramos um último resumo da solicitação
    print("\n================================")
    print("       CONFIRMAÇÃO DA CORRIDA")
    print("================================")

    print("Motorista:", motorista_encontrado.nome)
    print("Veículo:", motorista_encontrado.marca,
          motorista_encontrado.modelo)
    print("Placa:", motorista_encontrado.placa)
    print("Pagamento:", pagamento)
    print("Valor total: R$", round(corrida_provisoria.valor, 2))

    # O passageiro decide se deseja continuar ou cancelar a solicitação
    confirmar = input("\nDeseja confirmar sua corrida? (S/N): ").strip().upper()

    if confirmar != "S":

        print("\nTudo bem! Sua solicitação foi cancelada.")
        return

    # Se o passageiro confirmar, criamos a corrida definitiva
    nova_corrida = Corrida(
        passageiro_encontrado,
        motorista_encontrado,
        origem,
        destino,
        distancia,
        pagamento,
        quantidade_passageiros
    )

    # Depois que a corrida é confirmada, o motorista fica ocupado
    # Dessa maneira, ele não aparece em outra solicitação enquanto estiver ocupado
    motorista_encontrado.disponivel = False

    # Guardamos a corrida para que ela apareça no histórico
    lista_corridas.append(nova_corrida)

    # Mostramos que a solicitação foi realizada com sucesso
    print("\n================================")
    print("       SUA CORRIDA FOI CONFIRMADA!")
    print("================================")

    print("Passageiro:", passageiro_encontrado.nome)
    print("Motorista:", motorista_encontrado.nome)

    print("Veículo:", motorista_encontrado.marca,
          motorista_encontrado.modelo)

    print("Placa:", motorista_encontrado.placa)
    print("Saída:", origem)
    print("Destino:", destino)
    print("Distância:", distancia, "KM")
    print("Passageiros:", quantidade_passageiros)
    print("Forma de pagamento:", pagamento)

    print("Valor total: R$", round(nova_corrida.valor, 2))

    print("\nPronto! Sua corrida foi cadastrada.")
    print("Obrigado por escolher nosso aplicativo!")
    print("Boa viagem!")


# ----------------------------------------------------------
# HISTÓRICO DE CORRIDAS
# ----------------------------------------------------------
# Essa função permite consultar as viagens que já foram solicitadas
# e visualizar os principais dados de cada corrida
def ver_corridas():

    print("\n===== HISTÓRICO DE CORRIDAS =====")

    # Primeiro verificamos se já existe alguma viagem registrada
    if len(lista_corridas) == 0:

        print("Ainda não temos nenhuma corrida cadastrada.")
        return

    numero = 1

    # Percorremos a lista para mostrar os detalhes de cada viagem
    for corrida in lista_corridas:

        print("\n================================")
        print("CORRIDA NÚMERO:", numero)
        print("================================")

        print("Passageiro:", corrida.passageiro.nome)
        print("Motorista:", corrida.motorista.nome)

        print("Veículo:", corrida.motorista.marca,
              corrida.motorista.modelo)

        print("Placa:", corrida.motorista.placa)

        print("Idade do motorista:", corrida.motorista.idade)

        print("Telefone:", corrida.motorista.telefone)

        print("Avaliação do motorista:",
              corrida.motorista.avaliacao, "estrelas")

        print("Modalidade:", corrida.motorista.tipo_carro)

        print("Origem:", corrida.origem)
        print("Destino:", corrida.destino)

        print("Distância:", corrida.distancia, "KM")

        print("Quantidade de passageiros:",
              corrida.quantidade_passageiros)

        print("Forma de pagamento:", corrida.pagamento)

        print("Valor da corrida: R$", round(corrida.valor, 2))

        numero += 1


# ----------------------------------------------------------
# MENU PRINCIPAL
# ----------------------------------------------------------
# Esse é o menu que aparece quando o aplicativo é iniciado.
# O usuário escolhe o que deseja fazer e o programa chama
# a função responsável por aquela opção.
while True:

    print("\n================================")
    print("       APP DE TRANSPORTE")
    print("================================")

    print("1 - Cadastrar motorista")
    print("2 - Cadastrar passageiro")
    print("3 - Solicitar corrida")
    print("4 - Ver histórico de corridas")
    print("0 - Sair")

    opcao = input("\nO que deseja fazer? ")

    # Cada opção leva para uma parte diferente do aplicativo
    if opcao == "1":

        cadastrar_motorista()

    elif opcao == "2":

        cadastrar_passageiro()

    elif opcao == "3":

        pedir_corrida()

    elif opcao == "4":

        ver_corridas()

    elif opcao == "0":

        print("\nObrigado por utilizar nosso aplicativo!")
        print("Esperamos ver você novamente. Até a próxima!")

        break

    else:

        # Se o usuário digitar algo que não está no menu,
        # mostramos uma mensagem e voltamos para as opções
        print("\nOpção inválida! Escolha uma das opções do menu.")
