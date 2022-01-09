from conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(321, "Marco", 100.0, 1000.0)

conta2.transfere(10.0, conta)

print(conta.extrato())
print(conta2.extrato())