from Testes.Circulo import Circulo
cor = 'vermelho'
material = 'plastico'
c = Circulo(cor, material, 4)


print('Iniciando Teste\n\n')

print('Teste do trocaCor() \n\n')

assert c.cor == c.mostraCor(), f'erro, a cor:{cor} nao esta no objeto'
assert cor == c.mostraCor(), f'Erro, a cor: {cor} nao esta no objeto'

print('Teste do mostraCor(): OK\n\n')


print('Teste do area() \n\n')
assert c.raio == c.area(), f''





