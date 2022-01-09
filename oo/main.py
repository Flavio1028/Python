from conta import Conta

print(Conta.codigo_banco())
conta = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(321, "Marco", 100.0, 1000.0)

conta.saca(800)
conta.extrato()
