LIMITE_SAQUE_REAIS = 500
LIMITE_SAQUE_DIARIO = 3

nSaldo = float(2000)
aExtrato = []
iQtd_Saque = 0

def Validar_Saque(nValor_Saque: float) -> str:
    global iQtd_Saque, nSaldo
    if iQtd_Saque < LIMITE_SAQUE_DIARIO:
      if nValor_Saque > LIMITE_SAQUE_REAIS:
        cMsg_Validar_Saque = "Limite de saque Ultrapassado, o limite de saque é de R$ 500,00"
      elif nValor_Saque > nSaldo:
        cMsg_Validar_Saque = f"Saldo insuficiente seu saldo é de {nValor_Saque}"
      elif nValor_Saque <= 0:
        cMsg_Validar_Saque = "Por favor insirá um valor válido para realizar o Saque"
      else:
        cMsg_Validar_Saque = f"Saque no valor de {nValor_Saque} Realizado com Sucesso"
        aExtrato.append(f'Saque Realizado no valor de {nValor_Saque}')
        nSaldo = nSaldo - nValor_Saque
        iQtd_Saque = iQtd_Saque + 1
    else:
       cMsg_Validar_Saque = "Limite de Saque Diário atingido, obrigado pela preferência."
    return cMsg_Validar_Saque

def Validar_Deposito(nValor_Deposito: int) -> str:
    global nSaldo
    if nValor_Deposito <= 0: 
        cMsg_Validar_Deposito = "Por favor insirá um valor válido para realizar o Depósito"
    else:
       cMsg_Validar_Deposito = f"Depósito no valor de {nValor_Deposito} Realizado com Sucesso"
       aExtrato.append(f'Depósito Realizado no valor de {nValor_Deposito}')
       nSaldo = nSaldo + nValor_Deposito
    return cMsg_Validar_Deposito

def Retornar_Extrato():
   global nSaldo
   if not aExtrato:
      cMsg_Extrato = f"Nenhuma operação foi realizada até o momento {nSaldo}"
   else:
      cMsg_Extrato = "\n".join(aExtrato) + f"\nSaldo atual: {nSaldo}"
   return cMsg_Extrato