#=========================================================
# funções
#=========================================================

def saudacao(nome):
    print("Olá,", nome, "!")

saudacao("Carlos")
saudacao("Ana")

#=========================================================
# dicionários
#=========================================================

cliente = {
    "nome": "Miguel",
    "saldo": 100.0
}

print(cliente["nome"])
print(cliente["saldo"])

cliente["saldo"] = 150.0
print(cliente["saldo"])

#=========================================================
# clientes/constante
#=========================================================

clientes = [
    {"nome": "Miguel", "saldo": 150.0},
    {"nome": "Carlos", "saldo": 300.0}
]

clientes = []

VALOR_MINIMO_SAQUE = 1.0

#=========================================================
# criar conta
#=========================================================

def criar_conta():
    nome = input("Digite o nome do cliente: ")
    
    novo_cliente = {
        "nome": nome,
        "saldo": 0.0
    }
    
    clientes.append(novo_cliente)
    print("Conta criada com sucesso para:", nome)

#=========================================================
# buscar cliente
#=========================================================

def buscar_cliente(nome_procurado):
    for cliente in clientes:
        if cliente["nome"] == nome_procurado:
            return cliente
    return None

#=========================================================
# depositar
#=========================================================

def depositar():
    nome = input("Digite o nome do cliente: ")
    cliente = buscar_cliente(nome)
    
    if cliente is None:
        print("Cliente não encontrado!")
        return
        
    valor = float(input("Digite o valor do depósito: "))
    
    if valor <= 0:
        print("Valor de depósito inválido!")
        return
        
    cliente["saldo"] = cliente["saldo"] + valor
    print("Depósito realizado! Novo saldo:", cliente["saldo"])

#=========================================================
# sacar
#=========================================================

def sacar():
    nome = input("Digite o nome do cliente: ")
    cliente = buscar_cliente(nome)
    
    if cliente is None:
        print("Cliente não encontrado!")
        return
        
    valor = float(input("Digite o valor do saque: "))
    
    if valor < VALOR_MINIMO_SAQUE:
        print("Saldo insuficiente para realizar o saque!")
        return
        
    if valor > cliente["saldo"]:
        print("Saldo insuficiente para realizar o saque!")
        return
        
    cliente["saldo"] = cliente["saldo"] - valor
    print("Saque realizado! Novo Saldo:", cliente["saldo"])

#=========================================================
# consultar saldo
#=========================================================

def consultar_saldo():
    nome = input("Digite o nome do cliente: ")
    cliente = buscar_cliente(nome)
    
    if cliente is None:
        print("Cliente não encontrado!")
        return
        
    print("Saldo atual de", cliente["nome"], ": R$", cliente["saldo"])

#=========================================================
# menu ativo
#=========================================================

menu_ativo = True

while menu_ativo:
    print("\n===== DigiBank =====")
    print("1 - Criar Conta")
    print("2 - Depósito")
    print("3 - Saque")
    print("4 - Consultar Saldo")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        criar_conta()
    elif opcao == "2":
        depositar()
    elif opcao == "3":
        sacar()
    elif opcao == "4":
        consultar_saldo()
    elif opcao == "5":
        menu_ativo = False
        print("Obrigado por usar o DigiBank, até logo.")
    else:
        print("Opção inválida! Tente novamente.")
