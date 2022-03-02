from functools import total_ordering
from operator import attrgetter

idades = [15, 87, 32, 65, 56, 32, 49, 37]

print('Lista original: ', end="")
for numero in idades:
    print(f'{numero}', end=", ")

print('')

# Ordenação do menor para o maior
print(sorted(idades))

# Imprime a lista revertida
print(list(reversed(idades)))

# Ordenação do maior para o menor
print(sorted(idades, reverse=True))

nomes = ["Guilherme", "Daniela", "Paulo"]
print(sorted(nomes))

@total_ordering
class ContaSalario:

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  def deposita(self, valor):
    self._saldo += valor

  def __lt__(self, outro):
    return self._saldo < outro._saldo

  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in sorted(contas):
  print(conta)