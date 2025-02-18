numero_correto = 1
chute = int(input('Acerte que número estou pensando: '))

while chute != numero_correto:
    print('Ainda não! Continue tentando:')
    chute = int(input('Acerte que número estou pensando: '))

print('Parabéns! Você acertou!')


