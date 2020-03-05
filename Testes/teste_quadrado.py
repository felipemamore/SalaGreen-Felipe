from Testes.Quadrado import Quadrado


q = Quadrado('')
q.setLado(5)
print(q.calc_area())

print('Teste do quadrado iniciando \n\n')
assert set == q.calc_area(), f'Erro'
assert set == q.calc_area() == 25, f'erro'

print('Teste do calc_area(): OK')