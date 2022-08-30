



cliente = input('Digite seu nome: ')  # Indentificador cliente
print('Bem vindo a distribuidora virtual do Seu Zé: ',cliente)

produto = 0
qtd = 0
print('\n')
print('Promoção de inalguração')

print('\n', '-' * 18, 'PRODUTOS', '-' * 18)
print('|  PRODUTO  |     Marca     |       VALOR    |')
print('|    chop   |     Brahma    |       R$2,10   |')
print('|  cerveja  |    heineken   |       R$4,00   |')
print('|   whisky  |   Blue Label  |       R$999,00 |')
print('|    suco   |    Tampico    |       R$5,00   |')
print('|refigerante|    Guaraná    |       R$6,00   |')
print('-' * 47)

print('\n')

print('5% de desconto apartir de 10 produtos')
print('10% de desconto apartir de 100 produtos')
print('15% de desconto apartir de 1000 produtos')

produto = float(input('Digite valor do produto desejado: '))
qtd = float(input('Digite a quantidade que deseja comprar: '))

ValorTotal = produto * qtd

if qtd >= 1 and qtd <10 : 
  print('O valor total do produto é  R$:{:.2f} '.format (ValorTotal))
  print('Quantidade insuficiente para obter desconto.')
  

elif qtd >=10 and qtd<=99 :
  ValorDesconto = (ValorTotal - (ValorTotal*(5/100)))
  print('O valor do produto sem desconto R$:{:.2f} '.format (ValorTotal))
  print('O valor do produto com desconto R$:{:.2f} '.format (ValorDesconto),'(Desconto de 5%)')
  
elif qtd >99 and qtd <=999 :

  ValorDesconto = (ValorTotal - (ValorTotal*(10/100)))
  print('O valor do produto sem desconto R$:{:.2f} '.format (ValorTotal))
  print('O valor do produto com desconto R$:{:.2f} '.format (ValorDesconto),'(Desconto de 10%)')

else : #esse else ta aqui pq os valores possivel pra nao cair nos outros if só pode ser maior que 1000
  ValorDesconto = (ValorTotal - (ValorTotal*(15/100)))
  print('O valor do produto sem desconto R$:{:.2f} '.format (ValorTotal))
  print('O valor do produto com desconto R$:{:.2f} '.format (ValorDesconto),'(Desconto de 15%)')

print('Fim do programa, volte sempre!')