
# ==========================================================
# PROJETO: APLICATIVO DE TRANSPORTE
# TEMA: Aplicativo parecido com Uber
# OBJETIVO: Cadastrar motoristas e passageiros,
# solicitar corridas e calcular o valor de cada viagem.
# ==========================================================


# Classe que guarda as informações do motorista
# Aqui ficam os dados pessoais e as informações do carro
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

        # Todo motorista começa disponível para receber corridas
        self.disponivel = True


# Classe que guarda os dados do passageiro
class Passageiro:

    def __init__(self, nome, cpf):

        self.nome = nome
        self.cpf = cpf


# Classe responsável pelas corridas e pelo cálculo do preço
class Corrida:

    def __init__(self, passageiro, motorista, origem, destino,
                 distancia, pagamento):

        self.passageiro = passageiro
        self.motorista = motorista
        self.origem = origem
        self.destino = destino
        self.distancia = distancia
        self.pagamento = pagamento

        self.valor = 0

        # Assim que a corrida é criada, o preço já é calculado
        self.calcular_preco()

    def calcular_preco(self):

        # Valor cobrado no início de qualquer corrida
        bandeirada = 5.00

        # O preço por quilômetro muda de acordo com o carro escolhido
        if self.motorista.tipo_carro == "ECONOMY":

            preco_km = 1.50

        elif self.motorista.tipo_carro == "COMFORT":

            preco_km = 2.20

        else:

            preco_km = 3.50

        # Calcula o valor total da viagem
        self.valor = bandeirada + (self.distancia * preco_km)


# Listas utilizadas para guardar os cadastros e as corridas
# Por enquanto, as informações ficam salvas somente enquanto o programa está aberto

lista_motoristas = []
lista_passageiros = []
lista_corridas = []


# Cadastro de um novo motorista
def cadastrar_motorista():

    print("\n===== CADASTRO DE MOTORISTA =====")

    nome = input("Nome do motorista: ")

    # Verifica se o nome foi preenchido corretamente
    if len(nome.strip()) < 3:

        print("Nome inválido! Digite um nome com pelo menos 3 letras.")
        return

    # Solicita a idade do motorista para completar o cadastro
    try:

        idade = int(input("Idade do motorista: "))

        # Como se trata de um motorista, ele precisa ser maior de idade
        if idade < 18 or idade > 100:

            print("Idade inválida! O motorista precisa ter pelo menos 18 anos.")
            return

    except ValueError:

        print("Digite uma idade válida.")
        return

    # Guarda o telefone para que o passageiro possa identificar o contato
    telefone = input("Telefone do motorista: ").strip()

    placa = input("Placa do carro: ").strip().upper()

    # Confere se já existe outro carro com a mesma placa
    for motorista in lista_motoristas:

        if motorista.placa == placa:

            print("Essa placa já está cadastrada!")
            return

    # Agora vamos pegar as informações do veículo
    print("\n===== INFORMAÇÕES DO VEÍCULO =====")

    marca = input("Marca do carro: ").strip()
    modelo = input("Modelo do carro: ").strip()
    cor = input("Cor do carro: ").strip()

    try:

        ano = int(input("Ano do veículo: "))

        # Verifica se o ano informado faz sentido
        if ano < 1900 or ano > 2026:

            print("Ano do veículo inválido!")
            return

    except ValueError:

        print("Digite um ano válido.")
        return

    tipo = input(
        "Tipo do carro (ECONOMY, COMFORT ou BLACK): "
    ).strip().upper()

    # Confere se o tipo de carro escolhido existe no aplicativo
    if tipo not in ["ECONOMY", "COMFORT", "BLACK"]:

        print("Tipo de carro inválido! Tente novamente.")
        return

    # Informações adicionais para mostrar o perfil do motorista
    print("\n===== PERFIL DO MOTORISTA =====")

    try:

        avaliacao = float(input("Nota do motorista (0 a 5): "))

        # A nota precisa ficar dentro do limite de estrelas
        if avaliacao < 0 or avaliacao > 5:

            print("A avaliação precisa estar entre 0 e 5.")
            return

        viagens = int(input("Quantidade de viagens realizadas: "))

        if viagens < 0:

            print("Quantidade de viagens inválida!")
            return

    except ValueError:

        print("Digite valores válidos.")
        return

    # Cria o motorista com todas as informações preenchidas
    novo_motorista = Motorista(
        nome, placa, tipo, idade, marca, modelo,
        cor, ano, avaliacao, viagens, telefone
    )

    # Guarda o novo motorista na lista de cadastros
    lista_motoristas.append(novo_motorista)

    print("\nMotorista cadastrado com sucesso!")


# Cadastro de um novo passageiro
def cadastrar_passageiro():

    print("\n===== CADASTRO DE PASSAGEIRO =====")

    nome = input("Nome do passageiro: ")

    # Verifica se o nome foi preenchido corretamente
    if len(nome.strip()) < 3:

        print("Nome inválido! Digite um nome com pelo menos 3 letras.")
        return

    cpf = input("Digite o CPF (somente números): ").strip()

    # O CPF precisa ter exatamente 11 números
    if len(cpf) != 11 or not cpf.isdigit():

        print("CPF inválido! Digite os 11 números corretamente.")
        return

    # Verifica se esse CPF já foi utilizado em outro cadastro
    for passageiro in lista_passageiros:

        if passageiro.cpf == cpf:

            print("Esse CPF já está cadastrado!")
            return

    # Guarda os dados do passageiro na lista
    novo_passageiro = Passageiro(nome, cpf)

    lista_passageiros.append(novo_passageiro)

    print("\nPassageiro cadastrado com sucesso!")


# Mostra os dados do motorista e do veículo escolhido
# Essa parte funciona como o perfil que aparece para o passageiro
# antes de confirmar uma corrida
def mostrar_motorista(motorista):

    print("\n================================")
    print("       MOTORISTA ENCONTRADO")
    print("================================")

    print("\n===== PERFIL DO MOTORISTA =====")

    print("Nome:", motorista.nome)
    print("Idade:", motorista.idade, "anos")
    print("Telefone:", motorista.telefone)
    print("Avaliação:", motorista.avaliacao, "/ 5 estrelas")
    print("Viagens realizadas:", motorista.viagens)

    print("\n===== VEÍCULO DA CORRIDA =====")

    print("Marca:", motorista.marca)
    print("Modelo:", motorista.modelo)
    print("Cor:", motorista.cor)
    print("Ano:", motorista.ano)
    print("Placa:", motorista.placa)
    print("Categoria:", motorista.tipo_carro)

    print("\n===== INFORMAÇÕES DA CHEGADA =====")

    # Por enquanto, o tempo é apenas ilustrativo,
    # pois o programa ainda não utiliza GPS ou localização em tempo real
    tempo_chegada = 5

    print("Motorista a caminho!")
    print("Tempo estimado de chegada:", tempo_chegada, "minutos")


# Parte responsável por solicitar uma nova corrida
def pedir_corrida():

    print("\n===== SOLICITAR CORRIDA =====")

    # Antes de continuar, verifica se existem cadastros
    if len(lista_passageiros) == 0:

        print("Ainda não temos passageiros cadastrados.")
        return

    if len(lista_motoristas) == 0:

        print("Ainda não temos motoristas cadastrados.")
        return

    cpf = input("Digite o CPF do passageiro: ").strip()

    # Procura o passageiro pelo CPF informado
    passageiro_encontrado = None

    for passageiro in lista_passageiros:

        if passageiro.cpf == cpf:

            passageiro_encontrado = passageiro
            break

    if passageiro_encontrado == None:

        print("Não encontramos nenhum passageiro com esse CPF.")
        return

    # Pede as informações sobre o trajeto
    origem = input("Local de saída: ").strip()
    destino = input("Local de destino: ").strip()

    # Não permite continuar sem informar os locais
    if origem == "" or destino == "":

        print("Informe o local de saída e o destino.")
        return

    # Confere se a distância foi informada corretamente
    try:

        distancia = float(input("Distância da viagem em KM: "))

        if distancia <= 0:

            print("A distância precisa ser maior que zero.")
            return

    except ValueError:

        print("Distância inválida! Digite um número, como 8.5.")
        return

    tipo = input(
        "Qual tipo de carro deseja (ECONOMY, COMFORT ou BLACK)? "
    ).strip().upper()

    # Confere se a categoria escolhida existe no aplicativo
    if tipo not in ["ECONOMY", "COMFORT", "BLACK"]:

        print("Categoria inválida!")
        return

    # Cria uma lista separada somente com os motoristas
    # que estão livres e possuem o tipo de carro escolhido
    motoristas_disponiveis = []

    for motorista in lista_motoristas:

        if motorista.tipo_carro == tipo and motorista.disponivel == True:

            motoristas_disponiveis.append(motorista)

    # Se não tiver nenhum motorista livre, a corrida não pode continuar
    if len(motoristas_disponiveis) == 0:

        print("Não encontramos um motorista disponível desse tipo.")
        return

    # Mostra as opções para o passageiro escolher quem vai realizar a viagem
    print("\n===== MOTORISTAS DISPONÍVEIS =====")

    for i, motorista in enumerate(motoristas_disponiveis):

        print("\nMotorista número:", i + 1)
        print("Nome:", motorista.nome)
        print("Veículo:", motorista.marca, motorista.modelo)
        print("Cor:", motorista.cor)
        print("Avaliação:", motorista.avaliacao, "estrelas")

    # O passageiro escolhe o motorista que deseja
    try:

        escolha = int(input("\nEscolha o número do motorista: "))

        if escolha < 1 or escolha > len(motoristas_disponiveis):

            print("Opção inválida!")
            return

    except ValueError:

        print("Digite um número válido.")
        return

    # Guarda o motorista escolhido para utilizar nas próximas etapas
    motorista_encontrado = motoristas_disponiveis[escolha - 1]

    # Mostra os dados completos do motorista e do carro
    # antes de o passageiro confirmar a solicitação
    mostrar_motorista(motorista_encontrado)

    # Cria uma corrida provisória somente para calcular o preço
    # Assim, o passageiro consegue saber quanto vai pagar antes de confirmar
    corrida_provisoria = Corrida(
        passageiro_encontrado,
        motorista_encontrado,
        origem,
        destino,
        distancia,
        ""
    )

    print("\n===== RESUMO DA VIAGEM =====")

    print("Passageiro:", passageiro_encontrado.nome)
    print("Origem:", origem)
    print("Destino:", destino)
    print("Distância:", distancia, "KM")
    print("Categoria:", tipo)

    print("Valor da corrida: R$",
          round(corrida_provisoria.valor, 2))

    # O passageiro também pode escolher como deseja pagar
    print("\n===== FORMA DE PAGAMENTO =====")

    print("1 - Dinheiro")
    print("2 - PIX")
    print("3 - Cartão de crédito")
    print("4 - Cartão de débito")

    pagamento = input("Escolha a forma de pagamento: ")

    # Relaciona cada número com uma forma de pagamento
    formas_pagamento = {

        "1": "Dinheiro",
        "2": "PIX",
        "3": "Cartão de crédito",
        "4": "Cartão de débito"

    }

    # Confere se a opção escolhida está disponível
    if pagamento not in formas_pagamento:

        print("Forma de pagamento inválida!")
        return

    # Guarda o nome da forma de pagamento escolhida
    pagamento = formas_pagamento[pagamento]

    # Antes de cadastrar a corrida, mostra os últimos detalhes
    print("\n================================")
    print("       CONFIRMAR CORRIDA")
    print("================================")

    print("Motorista:", motorista_encontrado.nome)
    print("Carro:", motorista_encontrado.modelo)
    print("Placa:", motorista_encontrado.placa)
    print("Pagamento:", pagamento)
    print("Valor: R$", round(corrida_provisoria.valor, 2))

    # O passageiro pode confirmar ou desistir da solicitação
    confirmar = input(
        "\nDeseja confirmar essa corrida? (S/N): "
    ).strip().upper()

    if confirmar != "S":

        print("\nCorrida cancelada pelo passageiro.")
        return

    # Cria a corrida com todas as informações recebidas
    nova_corrida = Corrida(
        passageiro_encontrado,
        motorista_encontrado,
        origem,
        destino,
        distancia,
        pagamento
    )

    # Depois de aceitar a corrida, o motorista fica ocupado
    motorista_encontrado.disponivel = False

    # Guarda a nova corrida no histórico do aplicativo
    lista_corridas.append(nova_corrida)

    # Mostra o resumo da viagem para o passageiro
    print("\n================================")
    print("       CORRIDA CONFIRMADA!")
    print("================================")

    print("Passageiro:", passageiro_encontrado.nome)
    print("Motorista:", motorista_encontrado.nome)

    print("Veículo:", motorista_encontrado.marca,
          motorista_encontrado.modelo)

    print("Placa:", motorista_encontrado.placa)
    print("Saída:", origem)
    print("Destino:", destino)
    print("Distância:", distancia, "KM")

    print("Forma de pagamento:", pagamento)

    print("Valor total: R$", round(nova_corrida.valor, 2))

    print("\nSeu motorista foi confirmado!")
    print("Boa viagem!")


# Mostra todas as corridas que já foram solicitadas
def ver_corridas():

    print("\n===== HISTÓRICO DE CORRIDAS =====")

    # Verifica se existe alguma corrida cadastrada
    if len(lista_corridas) == 0:

        print("Nenhuma corrida foi realizada ainda.")
        return

    numero = 1

    # Passa por todas as corridas e mostra suas informações
    for corrida in lista_corridas:

        print("\nCorrida número:", numero)

        print("Passageiro:", corrida.passageiro.nome)
        print("Motorista:", corrida.motorista.nome)

        print("Veículo:", corrida.motorista.marca,
              corrida.motorista.modelo)

        print("Placa:", corrida.motorista.placa)

        print("Idade do motorista:", corrida.motorista.idade)

        print("Avaliação:", corrida.motorista.avaliacao, "estrelas")

        print("Trajeto:", corrida.origem, "até", corrida.destino)

        print("Distância:", corrida.distancia, "KM")

        print("Pagamento:", corrida.pagamento)

        print("Valor: R$", round(corrida.valor, 2))

        numero += 1


# Menu principal do aplicativo
while True:

    print("\n================================")
    print("       APP DE TRANSPORTE")
    print("================================")

    print("1 - Cadastrar motorista")
    print("2 - Cadastrar passageiro")
    print("3 - Solicitar corrida")
    print("4 - Ver histórico de corridas")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # Cada opção chama uma parte diferente do programa
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
        print("Até a próxima!")

        break

    else:

        print("\nOpção inválida! Escolha uma das opções do menu.")
