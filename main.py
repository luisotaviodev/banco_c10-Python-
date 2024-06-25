# [DEPOSITO]
#  - Depositar Valores positivos
#  - Todos os depositos devem serem exibios no extrato
# [SAQUE]
#  - Sistema deve Permitir 3 Saques diários
#  - Limite máximo de R$ 500,00 reais por saque
#  - Caso não tenha saldo dar mensagem de aviso
#  - Todos os saques devem serem exibidos no extrato
# [EXTRATO]
#  - Deve listar todos os depósitos e saques realizados na conta. No fim da lsitagem deve ser exibido o saldo atual da conta.
#    > Formato - R$ XXX.XX,
import DTUtilBanco

cNome = input("Olá seja Bem vindo ao banco C10+, para localizar a sua conta por favor digite o seu nome: ")
print('*'*100)
print(f"Conta localizada com Sucesso, seja bem vindo de volta {cNome}.")

while True:
  cOperacao = input(f"Selecione a operação que deseja realizar:\n [S] - SAQUE\n [D] - DEPÓSITO\n [E] - EXTRATO\n DIGITE 'SAIR' PARA FINALIZAR A OPREÇÃO\n").upper()
  if cOperacao == 'S':
    nValor_Saque = float(input("SAQUE\nPor favor digite o valor que deseja Sacar: "))
    print(DTUtilBanco.Validar_Saque(nValor_Saque))
  elif cOperacao == 'D':
    print("DEPÓSITO")
    iValor_Deposito = int(input("Por favor digite o valor que deseja Depositar: "))
    print(DTUtilBanco.Validar_Deposito(iValor_Deposito))
  elif cOperacao == 'E':
    print("EXTRATO")
    print(DTUtilBanco.Retornar_Extrato())
  elif cOperacao == 'SAIR':
    print("Operação finalizada, obrigado pela preferência.")
    break